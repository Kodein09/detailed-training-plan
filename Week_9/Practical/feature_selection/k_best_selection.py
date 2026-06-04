import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, RobustScaler


class PreprocessingData:
    def __init__(self, df: pd.DataFrame) -> None:
        self._df = df.copy()

    def scale_numeric(self) -> pd.DataFrame:
        scaler = RobustScaler()
        for col in self._df.columns:
            if np.issubdtype(self._df[col].dtype, np.number):
                if col in ['Survived', 'PassengerId']:
                    continue
                self._df[col] = self._df[col].fillna(self._df[col].median())
                self._df[col] = scaler.fit_transform(self._df[[col]])[:, 0]
        return self._df

    def label_encoder(self) -> pd.DataFrame:
        le = LabelEncoder()
        for col in self._df.columns:
            if self._df[col].dtype in ['object', 'category'] and self._df[col].nunique() > 3:
                self._df[col] = self._df[col].fillna('Unknown')
                self._df[col] = le.fit_transform(self._df[col].astype(str))
        return self._df

    def one_hot_encoder(self) -> pd.DataFrame:
        ohe = OneHotEncoder(sparse_output=False, dtype=int, handle_unknown='ignore')
        for col in self._df.columns:
            if self._df[col].nunique() <= 3 and self._df[col].dtype in ['object', 'category']:
                self._df[col] = self._df[col].fillna(self._df[col].mode()[0])
                self._df[col] = ohe.fit_transform(self._df[[col]])[:, 0]
        return self._df

    def pipeline(self) -> pd.DataFrame:
        self._df = self._df.drop(columns=['Ticket', 'Name', 'Cabin'], errors='ignore')
        self.scale_numeric()
        self.label_encoder()
        self.one_hot_encoder()
        return self._df

    def select_k_best(self, k: int = 5) -> str:
        X = self._df.drop(columns=['Survived', 'PassengerId'], errors='ignore')
        y = self._df['Survived']
        selector = SelectKBest(score_func=f_classif, k=k)
        pipeline = Pipeline([
            ('feature_selection', selector),
            ('model', LogisticRegression())
        ])
        pipeline.fit(X, y)
        selected_features = X.columns[pipeline.named_steps['feature_selection'].get_support()]
        return f"5 лучших признаков по вычислениям SelectKBest: {list(selected_features)}"


train_dataset = pd.read_csv("../train.csv")
prep = PreprocessingData(train_dataset)

clean_dataset = prep.pipeline()

print(f"--- Отбор признаков ---\n{prep.select_k_best()}\n")
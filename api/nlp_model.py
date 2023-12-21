from sentence_transformers import SentenceTransformer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def string_to_array(embed_str: str):
    res = embed_str.replace("[", "")
    res = res.replace("]", "")
    res = res.replace("\n", "")

    res = list(filter(None, [x for x in res.split(" ")]))

    return np.array([float(x) for x in res])


def predict_cv(vaccancy_text: str, model, df_cv: pd.DataFrame):
    result = ""
    tiny_sims = {}
    vaccancy_embedding = model.encode(vaccancy_text)

    for index, row in df_cv.iterrows():
        print(type(row["tiny_embedding"]))
        tiny_sims[index] = cosine_similarity([vaccancy_embedding, string_to_array(row["tiny_embedding"])])[0][1]
    
    tiny_sims = {k: v for k, v in sorted(tiny_sims.items(), key=lambda item: item[1], reverse=True)}

    best_cv = list(tiny_sims.items())[0:5]

    for i, val in enumerate(best_cv):
        result += f"Топ {i + 1} резюме - сходство {(val[1] * 100):.2f}:\n{df_cv.iloc[val[0]].cv_text}\n"

    return result


def predict_vaccancy(cv_text: str, model, df_vac: pd.DataFrame):
    result = ""
    tiny_sims = {}
    cv_embedding = model.encode(cv_text)
    
    for index, row in df_vac.iterrows():
        tiny_sims[index] = cosine_similarity([cv_embedding, string_to_array(row["tiny_embedding"])])[0][1]
    
    tiny_sims = {k: v for k, v in sorted(tiny_sims.items(), key=lambda item: item[1], reverse=True)}

    best_vaccancies = list(tiny_sims.items())[0:5]

    for i, val in enumerate(best_vaccancies):
        result += f"Топ {i + 1} вакансия - сходство {(val[1] * 100):.2f}:\n{df_vac.iloc[val[0]].vac_text}\n"

    return result
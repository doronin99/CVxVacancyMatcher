# CVxVacancyMatcher
The text-based service for the matching of job descriptions and CVs for enhanced recruitment precision [NLP course study project]

## Работа с данными

Создан датасет с текстами вакансий и резюме на основе данных hh.ru

- [Оригинальный датасет](https://drive.google.com/file/d/1rmkQVvLH9A5428o6ReziCTGGnlRrAnys/view?usp=sharing)

- [Итоговый датасет](https://drive.google.com/file/d/1usnDtA6_xeCDUmk3EuwffC5dcp28b6Iq/view?usp=sharing)

В дальнейшем были взяты другие данные, так как они несут в себе больше информации

- [Вакансии](https://www.kaggle.com/datasets/ivangurin/vacancyhh)

- [Резюме](https://drive.google.com/file/d/1ikA_Ht45fXD2w5dWZ9sGTSRl-UNeCVub/view?usp=share_link)

## Эксперименты

### Энкодеры

[Ноутбук](./experiments/embeddings.ipynb)

Были протестированы модели:
- rubert-tiny2
- paraphrase-multilingual-mpnet-base-v2

На основе табличных данных по шаблону было составлено поле с текстами вакансий/резюме. Для каждого текста были посчитаны эмбеддинги с помощью двух моделей, после чего выдавались рекомендации на основе косинусного сходства.

Модель **paraphrase-multilingual-mpnet-base-v2** показала себя немного лучше в случае поиска резюме по вакансии, в ином случае модель **rubert-tiny2** оказалась куда более точной.

### NER

[Ноутбук](./experiments/NER.ipynb)

Протестировали пакет [natasha](https://natasha.github.io/?ysclid=lqd17btfjp94158319) с целью выделения данных о локации из вакансий/резюме. Проблема в том, что зачастую захватываются лишние слова либо локации, которые связаны с предыдущим местом работы/местом учебы и т. д., которые будут только запутывать нас при подборе резюме/вакансии. Поэтому решили попробовать qusteion-answering модели, чтобы доставать данные о локациях из текста.

### QA модели

[Ноутбук](./experiments/QAmodels.ipynb)

### keyBERT

[Ноутбук](./experiments/keywords.ipynb)

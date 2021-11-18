import pandas as pd
import os


def analytics():
    path = os.path.join(os.path.dirname(__file__), 'input', 'test_data.csv')
    data = pd.read_csv(path, engine='python', encoding='utf-8', sep=',', dtype=str)

    data.columns = data.columns.str.lower()
    data = data.applymap(lambda x: x.strip().upper() if isinstance(x, str) else x)
    data = data.replace("\\N", "")

    data['userid'] = data['userid'].str.replace("+", "")
    data['first'] = data['first'].replace(dict.fromkeys(["..", "......"], ""))
    data['last'] = data['last'].replace(dict.fromkeys(["..", "......", "_", "-"], ""))
    data['last'] = data['last'].apply(lambda x: "" if x == "." else x)

    data['pin'] = data['pin'].apply(lambda x: "" if str(x).isupper() else x)
    data['pin'] = data['pin'].str.replace(",", "")
    data['pin'] = data['pin'].replace("......", "")

    data = data[data['userid'] != ""]

    data.to_csv(os.path.join(os.path.dirname(__file__), 'output', 'test_data_cleaned.csv'),
                index=False, encoding='utf-8')


def get_distinct_user_count():
    path = os.path.join(os.path.dirname(__file__), 'output', 'test_data_cleaned.csv')
    data = pd.read_csv(path, engine='python', encoding='utf-8', sep=',', dtype=str)

    print(f"Count of distinct users is: {data['userid'].drop_duplicates().shape[0]}")


def get_most_popular_lessons(grade):
    path = os.path.join(os.path.dirname(__file__), 'output', 'test_data_cleaned.csv')
    data = pd.read_csv(path, engine='python', encoding='utf-8', sep=',', dtype=str)

    grade_data = data[data['grade'] == grade]
    popular_lessons = grade_data.groupby(['grade', 'lessonnumber'], as_index=False).size()
    popular_lessons.rename(columns={"size": 'count'}, inplace=True)
    popular_lessons = popular_lessons.sort_values(['count'], ascending=False).head(5)
    print(popular_lessons)


def get_top_five_states_language_count():
    path = os.path.join(os.path.dirname(__file__), 'output', 'test_data_cleaned.csv')
    data = pd.read_csv(path, engine='python', encoding='utf-8', sep=',', dtype=str)
    state_wise_group = data.groupby(['state'], as_index=False).size().head(5)
    print(state_wise_group)

    for state in state_wise_group['state']:
        state_data = data[data['state'] == state]
        language_breakup = state_data.groupby(['state', 'language'], as_index=False).size()
        print(language_breakup)


if __name__ == "__main__":
    analytics()
    get_distinct_user_count()
    get_most_popular_lessons("4")
    get_top_five_states_language_count()

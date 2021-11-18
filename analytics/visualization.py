import matplotlib.pyplot as plt
import pandas as pd
import os


def state_wise_user_count():
    x = []
    y = []
    file_path = os.path.join(os.path.dirname(__file__), 'output', 'test_data_cleaned.csv')
    data = pd.read_csv(file_path, engine='python', sep=',', encoding='utf-8')

    user_count = data.groupby(['state'], as_index=False).size().head(5)
    plt.bar(user_count['state'], user_count['size'], color='b', width=0.8, label='user_count')
    plt.xlabel('States')
    plt.ylabel('User Count')
    plt.title('Count of users per state')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    state_wise_user_count()
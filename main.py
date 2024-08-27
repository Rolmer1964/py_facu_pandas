import pandas as pd
from IPython.display import display


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def cria_series():
    return pd.Series([10.2, -1, None, 15, 23.4])

def cria_dictionary():
    return {'Nome': ['Luan', 'Levy', 'Aurora'],
            'idade': [15, 14, 1],
            'Altura': [1.78, 1.71, 0.51],
            'Naturalidade': ['Manaus', 'Manaus', 'London']
            }

def manipulaSeries():
    # Cria uma series
    series_dados = cria_series()

    # cria um dictionary
    dictionary_dados = cria_dictionary()

    # extrai um dataframe a partir do dictionary
    df = pd.DataFrame(dictionary_dados)

    trump_df = pd.read_csv("trump.csv")

    print(f"Elementos da series {series_dados}")
    print(f"quantidade de linhas da series {series_dados.shape}")
    print(f"Tipo de dados da series {series_dados.dtypes}")
    print(f"Os valores da series são únicos {series_dados.is_unique}")
    print(f"Existem valores nulos na series {series_dados.hasnans}")
    print(f"Quantos valores existem na series {series_dados.count()}")
    print(f"Mínimo valor da series {series_dados.min()}")
    print(f"Máximo valor da series {series_dados.max()}")
    print(f"Valor médio da series {series_dados.mean()}")
    print(f"Desvio padrão da series {series_dados.std()}")
    print(f"Mediana da series {series_dados.median()}")
    print(f"Descrição da series {series_dados.describe()}")

    print(f"Exibindo o data frame com print \n {df}")

    print("Exibindo o data frame com display")
    display(df)

    print("Exibindo o data frame com twites do trump")
    display(trump_df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    manipulaSeries()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

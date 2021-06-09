# Create Dummies
#import sys
"""new_path = '../scripts/'
if new_path not in sys.path:
    sys.path.append(new_path)"""

import pandas as pd 

def transform_dummies(df, var_name):

    dummy = pd.get_dummies(df[var_name], prefix=var_name)
    df = df.drop(var_name, axis = 1)
    df = pd.concat([df, dummy], axis = 1)

    return df


from sklearn.preprocessing import OrdinalEncoder

def transform_ordinal(df, var_name):
# Creamos el codif(icador indicandole el orden de la variables
    encoder = OrdinalEncoder()

# Ajustamos el codificador con la variable education y la transformamos
    encoder.fit(df[[var_name]])
    df[f"{var_name}-encoded"] = encoder.transform(df[[var_name]])
    df = df.drop(var_name)
    return df
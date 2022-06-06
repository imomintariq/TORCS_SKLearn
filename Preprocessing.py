import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv('CSVFILE.csv')
df.dropna(inplace=True)

df = df.replace(['[]'], '0')
df = df.replace(['[None]'], '0')
df['angle'] = df['angle'].str.strip('[]')
df['damage'] = df['damage'].str.strip('[]')
df['curLapTime'] = df['curLapTime'].str.strip('[]')
df['distFromStart'] = df['distFromStart'].str.strip('[]')
df['distRaced'] = df['distRaced'].str.strip('[]')
df['fuel'] = df['fuel'].str.strip('[]')
# print(df['gear_1'])
df['gear_1'] = df['gear_1'].str.strip('[]')
df['rpm'] = df['rpm'].str.strip('[]')
df['lastLapTime'] = df['lastLapTime'].str.strip('[]')
df['racePos'] = df['racePos'].str.strip('[]')
df['speedX'] = df['speedX'].str.strip('[]')
df['speedY'] = df['speedY'].str.strip('[]')
df['speedZ'] = df['speedZ'].str.strip('[]')
df['z'] = df['z'].str.strip('[]')
df['x'] = df['x'].str.strip('[]')
df['y'] = df['y'].str.strip('[]')
df['roll'] = df['roll'].str.strip('[]')
df['pitch'] = df['pitch'].str.strip('[]')
df['yaw'] = df['yaw'].str.strip('[]')
df['z'] = df['z'].str.strip('[]')
df['speedGlobalX'] = df['speedGlobalX'].str.strip('[]')
df['speedGlobalY'] = df['speedGlobalY'].str.strip('[]')
df['trackPos'] = df['trackPos'].str.strip('[]')
df['accel'] = df['accel'].str.strip('[]')
df['brake'] = df['brake'].str.strip('[]')
df['steer'] = df['steer'].str.strip('[]')
df['gear_2'] = df['gear_2'].str.strip('[]')
df['gas'] = df['gas'].str.strip('[]')
df['clutch'] = df['clutch'].str.strip('[]')
df['meta'] = df['meta'].str.strip('[]')

# print(df)

df['track'] = df['track'].str.strip('[[]]')
df2 = df['track'].str.split(',', expand=True)
df = df.drop("track", axis=1)
i = 0
for c in df2:
    df2.rename(columns={c: 'track' + str(i)}, inplace=True)
    i += 1
df = df.join(df2)

df['wheelSpinVel'] = df['wheelSpinVel'].str.strip('[[]]')
df4 = df['wheelSpinVel'].str.split(',', expand=True)
df = df.drop("wheelSpinVel", axis=1)
i = 0
for c in df4:
    df4.rename(columns={c: 'wheelSpinVel' + str(i)}, inplace=True)
    i += 1
df = df.join(df4)

df['focus_1'] = df['focus_1'].str.strip('[[]]')
df5 = df['focus_1'].str.split(',', expand=True)
df = df.drop("focus_1", axis=1)
i = 0
for c in df5:
    df5.rename(columns={c: 'focus_1' + str(i)}, inplace=True)
    i += 1
df = df.join(df5)

df['focus_2'] = df['focus_2'].str.strip('[[]]')
df6 = df['focus_2'].str.split(',', expand=True)
df = df.drop("focus_2", axis=1)
i = 0
for c in df6:
    df6.rename(columns={c: 'focus_2' + str(i)}, inplace=True)
    i += 1
df = df.join(df6)


# df['opponents'] = df['opponents'].str.strip('[[]]')
# df7 = df['opponents'].str.split(',', expand=True)
df = df.drop("opponents", axis=1)
# i = 0
# for c in df7:
#     df7.rename(columns={c: 'opponents' + str(i)}, inplace=True)
#     i += 1
# df = df.join(df7)

# Reordering Columns
column_to_reorder = df.pop('meta')
df.insert(0, 'meta', column_to_reorder)

for i in range(0, 5):
    column_to_reorder = df.pop('focus_2' + str(i))
    df.insert(0, 'focus_2' + str(i), column_to_reorder)

column_to_reorder = df.pop('clutch')
df.insert(0, 'clutch', column_to_reorder)

column_to_reorder = df.pop('gas')
df.insert(0, 'gas', column_to_reorder)

column_to_reorder = df.pop('gear_2')
df.insert(0, 'gear_2', column_to_reorder)

column_to_reorder = df.pop('brake')
df.insert(0, 'brake', column_to_reorder)

column_to_reorder = df.pop('steer')
df.insert(0, 'steer', column_to_reorder)

column_to_reorder = df.pop('accel')
df.insert(0, 'accel', column_to_reorder)

# print("hello")
# print(df)

X = df.iloc[:, 12:]
Y = df.iloc[:, :12, ]

print(X)

df = df.astype(float)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=44)

from sklearn.tree import DecisionTreeRegressor

regressor = DecisionTreeRegressor(random_state=44)
regressor.fit(X_train, Y_train)

y_pred = regressor.predict(X_test)

from sklearn.metrics import mean_squared_error
import numpy as np

rmse = np.sqrt(mean_squared_error(Y_test, y_pred))
print(rmse)

import pickle

pickle.dump(regressor, open('model3.pkl', 'wb'))

pickled_model = pickle.load(open('model3.pkl', 'rb'))

print(y_pred)

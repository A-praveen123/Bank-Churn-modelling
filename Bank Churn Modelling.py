{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "28283d5c-ac25-446b-836d-6132737c5f8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e215b257-ea7a-44b8-8188-b5d493fed1dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ac9b8491-ea2c-4fc6-8aaa-9ebb71cceeeb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5a274f6a-d356-42c7-87bb-14a4bfa519a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7b549e90-0e94-4fbb-82ee-06ec406c39f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "3a73f93c-1054-4a3a-83a8-0b63b27b41fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(r\"C:\\Users\\Admin\\Documents\\ms excel\\Bank Churn Modelling.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "3be38cd9-0247-40c2-9941-4e088e439737",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>Num Of Products</th>\n",
       "      <th>Has Credit Card</th>\n",
       "      <th>Is Active Member</th>\n",
       "      <th>Estimated Salary</th>\n",
       "      <th>Churn</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>15634602</td>\n",
       "      <td>Hargrave</td>\n",
       "      <td>619</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>15647311</td>\n",
       "      <td>Hill</td>\n",
       "      <td>608</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>15619304</td>\n",
       "      <td>Onio</td>\n",
       "      <td>502</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>8</td>\n",
       "      <td>159660.80</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113931.57</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>15701354</td>\n",
       "      <td>Boni</td>\n",
       "      <td>699</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>39</td>\n",
       "      <td>1</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>93826.63</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>15737888</td>\n",
       "      <td>Mitchell</td>\n",
       "      <td>850</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>43</td>\n",
       "      <td>2</td>\n",
       "      <td>125510.82</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>79084.10</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   CustomerId   Surname  CreditScore Geography  Gender  Age  Tenure  \\\n",
       "0    15634602  Hargrave          619    France  Female   42       2   \n",
       "1    15647311      Hill          608     Spain  Female   41       1   \n",
       "2    15619304      Onio          502    France  Female   42       8   \n",
       "3    15701354      Boni          699    France  Female   39       1   \n",
       "4    15737888  Mitchell          850     Spain  Female   43       2   \n",
       "\n",
       "     Balance  Num Of Products  Has Credit Card  Is Active Member  \\\n",
       "0       0.00                1                1                 1   \n",
       "1   83807.86                1                0                 1   \n",
       "2  159660.80                3                1                 0   \n",
       "3       0.00                2                0                 0   \n",
       "4  125510.82                1                1                 1   \n",
       "\n",
       "   Estimated Salary  Churn  \n",
       "0         101348.88      1  \n",
       "1         112542.58      0  \n",
       "2         113931.57      1  \n",
       "3          93826.63      0  \n",
       "4          79084.10      0  "
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "272eab82-f594-4d14-86e6-04f031d112f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 10000 entries, 15634602 to 15628319\n",
      "Data columns (total 12 columns):\n",
      " #   Column            Non-Null Count  Dtype  \n",
      "---  ------            --------------  -----  \n",
      " 0   Surname           10000 non-null  object \n",
      " 1   CreditScore       10000 non-null  int64  \n",
      " 2   Geography         10000 non-null  int64  \n",
      " 3   Gender            10000 non-null  object \n",
      " 4   Age               10000 non-null  int64  \n",
      " 5   Tenure            10000 non-null  int64  \n",
      " 6   Balance           10000 non-null  float64\n",
      " 7   Num Of Products   10000 non-null  int64  \n",
      " 8   Has Credit Card   10000 non-null  int64  \n",
      " 9   Is Active Member  10000 non-null  int64  \n",
      " 10  Estimated Salary  10000 non-null  float64\n",
      " 11  Churn             10000 non-null  int64  \n",
      "dtypes: float64(2), int64(8), object(2)\n",
      "memory usage: 1015.6+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "4672f6e2-c7be-4eac-bdbe-f148ccd17b78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated('CustomerId').sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "b7a4f0b9-bb68-474a-872f-4a557e499b02",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.set_index(\"CustomerId\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09bc01ab-5fa3-4e5e-a3a0-6c1833e728d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#ENCODING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "eeb392c7-987e-4035-bd1d-00a3f423e1d6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Geography\n",
       "France     5014\n",
       "Germany    2509\n",
       "Spain      2477\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Geography'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "6d46f1e0-1bfd-41d4-a395-ef8f2c9d3540",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.replace({'Geography':{'France':2, 'Germany':1, 'Spain' :0}}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "4eaf0775-a38d-41f4-9fed-4905c1287842",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Gender\n",
       "Male      5457\n",
       "Female    4543\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Gender\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "bc68fecf-f30f-4de0-a315-040b7026278e",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.replace({\"Gender\": {\"Male\": 0, \"Female\":1}},inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "9d0b9609-ee1b-45c5-a739-0994f087d894",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.replace({\"Num of products\": {1:0, 2:1, 3:1, 4:1 }}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "e1ab4b5d-a40c-44cf-b421-81d7db6e4cc0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Has Credit Card\n",
       "1    7055\n",
       "0    2945\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Has Credit Card\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "8e43b02d-471b-40d0-a058-c7f92086d3d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Is Active Member\n",
       "1    5151\n",
       "0    4849\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Is Active Member\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "0cd1cc4a-ae33-4317-a819-f592088a1620",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Churn\n",
       "0    3117\n",
       "1     500\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[(df[\"Balance\"]==0), 'Churn'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "0adc51fd-9246-4f99-a7a4-6f75c2acc108",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>Num Of Products</th>\n",
       "      <th>Has Credit Card</th>\n",
       "      <th>Is Active Member</th>\n",
       "      <th>Estimated Salary</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Churn</th>\n",
       "      <th>Geography</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"3\" valign=\"top\">0</th>\n",
       "      <th>0</th>\n",
       "      <td>2064</td>\n",
       "      <td>2064</td>\n",
       "      <td>2064</td>\n",
       "      <td>2064</td>\n",
       "      <td>2064</td>\n",
       "      <td>2064</td>\n",
       "      <td>2064</td>\n",
       "      <td>2064</td>\n",
       "      <td>2064</td>\n",
       "      <td>2064</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1695</td>\n",
       "      <td>1695</td>\n",
       "      <td>1695</td>\n",
       "      <td>1695</td>\n",
       "      <td>1695</td>\n",
       "      <td>1695</td>\n",
       "      <td>1695</td>\n",
       "      <td>1695</td>\n",
       "      <td>1695</td>\n",
       "      <td>1695</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4204</td>\n",
       "      <td>4204</td>\n",
       "      <td>4204</td>\n",
       "      <td>4204</td>\n",
       "      <td>4204</td>\n",
       "      <td>4204</td>\n",
       "      <td>4204</td>\n",
       "      <td>4204</td>\n",
       "      <td>4204</td>\n",
       "      <td>4204</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"3\" valign=\"top\">1</th>\n",
       "      <th>0</th>\n",
       "      <td>413</td>\n",
       "      <td>413</td>\n",
       "      <td>413</td>\n",
       "      <td>413</td>\n",
       "      <td>413</td>\n",
       "      <td>413</td>\n",
       "      <td>413</td>\n",
       "      <td>413</td>\n",
       "      <td>413</td>\n",
       "      <td>413</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>814</td>\n",
       "      <td>814</td>\n",
       "      <td>814</td>\n",
       "      <td>814</td>\n",
       "      <td>814</td>\n",
       "      <td>814</td>\n",
       "      <td>814</td>\n",
       "      <td>814</td>\n",
       "      <td>814</td>\n",
       "      <td>814</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>810</td>\n",
       "      <td>810</td>\n",
       "      <td>810</td>\n",
       "      <td>810</td>\n",
       "      <td>810</td>\n",
       "      <td>810</td>\n",
       "      <td>810</td>\n",
       "      <td>810</td>\n",
       "      <td>810</td>\n",
       "      <td>810</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Surname  CreditScore  Gender   Age  Tenure  Balance  \\\n",
       "Churn Geography                                                        \n",
       "0     0             2064         2064    2064  2064    2064     2064   \n",
       "      1             1695         1695    1695  1695    1695     1695   \n",
       "      2             4204         4204    4204  4204    4204     4204   \n",
       "1     0              413          413     413   413     413      413   \n",
       "      1              814          814     814   814     814      814   \n",
       "      2              810          810     810   810     810      810   \n",
       "\n",
       "                 Num Of Products  Has Credit Card  Is Active Member  \\\n",
       "Churn Geography                                                       \n",
       "0     0                     2064             2064              2064   \n",
       "      1                     1695             1695              1695   \n",
       "      2                     4204             4204              4204   \n",
       "1     0                      413              413               413   \n",
       "      1                      814              814               814   \n",
       "      2                      810              810               810   \n",
       "\n",
       "                 Estimated Salary  \n",
       "Churn Geography                    \n",
       "0     0                      2064  \n",
       "      1                      1695  \n",
       "      2                      4204  \n",
       "1     0                       413  \n",
       "      1                       814  \n",
       "      2                       810  "
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(['Churn', 'Geography']).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "3578ddfa-74ee-4851-8d14-b727d8a39d4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#DEFINE LABEL AND FEATURES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "f5f55f40-6430-4a33-8571-e79907fe48c2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Surname', 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure',\n",
       "       'Balance', 'Num Of Products', 'Has Credit Card', 'Is Active Member',\n",
       "       'Estimated Salary', 'Churn'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "b4fdbc76-e81a-456e-afe8-f93039079bcf",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = df.drop(['Surname', 'Churn'], axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "cc2aebe8-58d2-48bf-bf2f-2098a37458fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "y = df[\"Churn\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "67f7b81e-85c8-4281-89c5-f6d1e110bb69",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((10000, 10), (10000,))"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.shape, y.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "878b4347-ba70-490d-9086-22d7528a7708",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Churn\n",
       "0    7963\n",
       "1    2037\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Churn'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "adf845db-13c7-4e0c-897f-91f6876191cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x ='Churn', data = df);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "de704b02-150c-43a9-b4fa-a766e4e332db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((10000, 10), (10000,))"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.shape, y.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "56029fae-ce05-4ba5-be7e-7099e09f1469",
   "metadata": {},
   "outputs": [],
   "source": [
    "#RANDOM UNDER SAMPLING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "a965b973-ea8f-4b01-8d0a-666219dd66f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "from imblearn.under_sampling import RandomUnderSampler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "eeaa8557-a12b-4796-b42c-2aee045fa7e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "rus = RandomUnderSampler(random_state=2529)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "8f8d7eec-6bb1-4032-a289-0cd267d09711",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_rus, y_rus = rus.fit_resample(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "9c504fe9-c85a-45e5-af51-c3a52f5d4ff1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((4074, 10), (4074,), (10000, 10), (10000,))"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_rus.shape, y_rus.shape, x.shape, y.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "949aed49-8eb5-4a40-aba5-a8d9a12026a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Churn\n",
       "0    7963\n",
       "1    2037\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "50cb4280-727f-4a06-a25e-254ddc273b3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Churn\n",
       "0    2037\n",
       "1    2037\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_rus.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "502a056a-c0f0-4422-9ade-bc3a4c65b112",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='Frequency'>"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkQAAAGdCAYAAADzOWwgAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/TGe4hAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAw0klEQVR4nO3deXQUZb7/8U+T0M0ySdhMOvkZw6KA7BI0ZgSEgUmADC4wV5FVjSAaXIgLk5GBCF6CQRlQGbjOsOiZIMi9iA4gkrAqBBWkBYNG2Yxc0gEF0iQMWev3hyd9bcOWJkkn1Pt1Tp2Tep5vV33rGZz+nOrqxGIYhiEAAAATa+DrBgAAAHyNQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEzP39cN1Afl5eU6fvy4AgICZLFYfN0OAAC4AoZh6OzZswoLC1ODBpe+B0QgugLHjx9XeHi4r9sAAABe+OGHH3T99ddfsoZAdAUCAgIk/byggYGBPu4GAABcCZfLpfDwcPf7+KUQiK5AxcdkgYGBBCIAAOqZK3nchYeqAQCA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6fn7ugFIrf+0ztctVNnR2XG+bgEAcBG8r1Qdd4gAAIDp+TQQpaSk6NZbb1VAQICCg4N1zz33KDs726Pm/PnzSkhIUMuWLfWb3/xGw4cPV15enkdNTk6O4uLi1KRJEwUHB+u5555TaWmpR83WrVvVs2dP2Ww23XjjjVq2bFlNXx4AAKgnfBqItm3bpoSEBO3atUvp6ekqKSlRTEyMCgsL3TWTJ0/Wv/71L61atUrbtm3T8ePHNWzYMPd8WVmZ4uLiVFxcrJ07d+qtt97SsmXLNG3aNHfNkSNHFBcXp/79+8vhcOjpp5/WI488oo8++qhWrxcAANRNFsMwDF83UeHkyZMKDg7Wtm3b1LdvX+Xn5+u6667T8uXL9cc//lGS9M033+jmm29WZmambr/9dn344Yf6wx/+oOPHjyskJESStGjRIk2ZMkUnT56U1WrVlClTtG7dOn311Vfuc40YMUJnzpzRhg0bLtuXy+VSUFCQ8vPzFRgYWO3XzWe9AIDqxPvKz6ry/l2nniHKz8+XJLVo0UKStGfPHpWUlGjgwIHumo4dO+qGG25QZmamJCkzM1Ndu3Z1hyFJio2NlcvlUlZWlrvml8eoqKk4BgAAMLc68y2z8vJyPf3007rjjjvUpUsXSZLT6ZTValWzZs08akNCQuR0Ot01vwxDFfMVc5eqcblc+ve//63GjRt7zBUVFamoqMi973K5rv4CAQBAnVVn7hAlJCToq6++0ooVK3zdilJSUhQUFOTewsPDfd0SAACoQXUiEE2aNElr167Vli1bdP3117vH7Xa7iouLdebMGY/6vLw82e12d82vv3VWsX+5msDAwEp3hyQpKSlJ+fn57u2HH3646msEAAB1l08DkWEYmjRpkt577z1t3rxZbdq08ZiPjIxUw4YNtWnTJvdYdna2cnJyFB0dLUmKjo7W/v37deLECXdNenq6AgMD1alTJ3fNL49RUVNxjF+z2WwKDAz02AAAwLXLp88QJSQkaPny5Xr//fcVEBDgfuYnKChIjRs3VlBQkOLj45WYmKgWLVooMDBQTzzxhKKjo3X77bdLkmJiYtSpUyeNGTNGqampcjqdmjp1qhISEmSz2SRJEydO1BtvvKHnn39eDz/8sDZv3qx3331X69bVv6fwAQBA9fPpHaKFCxcqPz9f/fr1U2hoqHtbuXKlu+avf/2r/vCHP2j48OHq27ev7Ha7Vq9e7Z738/PT2rVr5efnp+joaI0ePVpjx47VjBkz3DVt2rTRunXrlJ6eru7du+vVV1/VP/7xD8XGxtbq9QIAgLqpTv0eorqK30NUGb+HCADqLt5XflZvfw8RAACALxCIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6RGIAACA6fk0EG3fvl1Dhw5VWFiYLBaL1qxZ4zFvsVguuM2ZM8dd07p160rzs2fP9jjOvn371KdPHzVq1Ejh4eFKTU2tjcsDAAD1hE8DUWFhobp3764FCxZccD43N9djW7JkiSwWi4YP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ZV8fERGh9evX10RrAADgGlBvniECAACoKQQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgegQiAABgenU6ECUnJ8tisXhsHTt2dM+fP39eCQkJatmypX7zm99o+PDhysvL8zhGTk6O4uLi1KRJEwUHB+u5555TaWlpbV8KAACow/x93cDldO7cWRkZGe59f///a3ny5Mlat26dVq1apaCgIE2aNEnDhg3Tjh07JEllZWWKi4uT3W7Xzp07lZubq7Fjx6phw4aaNWtWrV8LAACom+p8IPL395fdbq80np+fr8WLF2v58uX63e9+J0launSpbr75Zu3atUu33367Nm7cqAMHDigjI0MhISHq0aOHZs6cqSlTpig5OVlWq7W2LwcAANRBdfojM0n67rvvFBYWprZt22rUqFHKycmRJO3Zs0clJSUaOHCgu7Zjx4664YYblJmZKUnKzMxU165dFRIS4q6JjY2Vy+VSVlbWRc9ZVFQkl8vlsQEAgGtXnQ5EUVFRWrZsmTZs2KCFCxfqyJEj6tOnj86ePSun0ymr1apmzZp5vCYkJEROp1OS5HQ6PcJQxXzF3MWkpKQoKCjIvYWHh1fvhQEAgDqlTn9kNnjwYPfP3bp1U1RUlCIiIvTuu++qcePGNXbepKQkJSYmuvddLhehCACAa1idvkP0a82aNVP79u118OBB2e12FRcX68yZMx41eXl57meO7HZ7pW+dVexf6LmkCjabTYGBgR4bAAC4dtWrQFRQUKBDhw4pNDRUkZGRatiwoTZt2uSez87OVk5OjqKjoyVJ0dHR2r9/v06cOOGuSU9PV2BgoDp16lTr/QMAgLqpTn9k9uyzz2ro0KGKiIjQ8ePHNX36dPn5+emBBx5QUFCQ4uPjlZiYqBYtWigwMFBPPPGEoqOjdfvtt0uSYmJi1KlTJ40ZM0apqalyOp2aOnWqEhISZLPZfHx1AACgrqjTgejYsWN64IEH9NNPP+m6665T7969tWvXLl133XWSpL/+9a9q0KCBhg8frqKiIsXGxupvf/ub+/V+fn5au3atHnvsMUVHR6tp06YaN26cZsyY4atLAgAAdVCdDkQrVqy45HyjRo20YMECLViw4KI1ERERWr9+fXW3BgAAriH16hkiAACAmkAgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAApkcgAgAAplenA1FKSopuvfVWBQQEKDg4WPfcc4+ys7M9avr16yeLxeKxTZw40aMmJydHcXFxatKkiYKDg/Xcc8+ptLS0Ni8FAADUYf6+buBStm3bpoSEBN16660qLS3Vn//8Z8XExOjAgQNq2rSpu278+PGaMWOGe79Jkybun8vKyhQXFye73a6dO3cqNzdXY8eOVcOGDTVr1qxavR4AAFA31elAtGHDBo/9ZcuWKTg4WHv27FHfvn3d402aNJHdbr/gMTZu3KgDBw4oIyNDISEh6tGjh2bOnKkpU6YoOTlZVqu1Rq8BAADUfXX6I7Nfy8/PlyS1aNHCYzwtLU2tWrVSly5dlJSUpHPnzrnnMjMz1bVrV4WEhLjHYmNj5XK5lJWVdcHzFBUVyeVyeWwAAODaVafvEP1SeXm5nn76ad1xxx3q0qWLe3zkyJGKiIhQWFiY9u3bpylTpig7O1urV6+WJDmdTo8wJMm973Q6L3iulJQUvfjiizV0JQAAoK6pN4EoISFBX331lT755BOP8QkTJrh/7tq1q0JDQzVgwAAdOnRI7dq18+pcSUlJSkxMdO+7XC6Fh4d71zgAAKjz6sVHZpMmTdLatWu1ZcsWXX/99ZesjYqKkiQdPHhQkmS325WXl+dRU7F/seeObDabAgMDPTYAAHDtqtOByDAMTZo0Se+99542b96sNm3aXPY1DodDkhQaGipJio6O1v79+3XixAl3TXp6ugIDA9WpU6ca6RsAANQvdfojs4SEBC1fvlzvv/++AgIC3M/8BAUFqXHjxjp06JCWL1+u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lztEML3Zs2drxYoVeu+999SoUSNft3PNOHv2rMaMGaO///3vatWqla/buaaVl5crODhYb775piIjI3X//ffrhRde0KJFi3zd2jVn69atmjVrlv72t7/piy++0OrVq7Vu3TrNnDnT163hKnGHqAa1atVKfn5+ysvL8xjPy8uT3W6/4GvsdnuV6uHdOld45ZVXNHv2bGVkZKhbt2412Wa9V9V1PnTokI4ePaqhQ4e6x8rLyyVJ/v7+ys7OVrt27Wq26XrIm3/PoaGhatiwofz8/NxjN998s5xOp4qLi2W1Wmu05/rKm7X+y1/+ojFjxuiRRx6RJHXt2lWFhYWaMGGCXnjhBTVowH2Gq3Wx98HAwMAauzskcYeoRlmtVkVGRmrTpk3usfLycm3atEnR0dEXfE10dLRHvSSlp6dftB7erbMkpaamaubMmdqwYYN69epVG63Wa1Vd544dO2r//v1yOBzu7a677lL//v3lcDgUHh5em+3XG978e77jjjt08OBBd+CUpG+//VahoaGEoUvwZq3PnTtXKfRUBFGDPw1aLXz2Plijj2zDWLFihWGz2Yxly5YZBw4cMCZMmGA0a9bMcDqdhmEYxpgxY4w//elP7vodO3YY/v7+xiuvvGJ8/fXXxvTp0/na/RWo6jrPnj3bsFqtxn//938bubm57u3s2bO+uoR6oarr/Gt8y+zKVHWdc3JyjICAAGPSpElGdna2sXbtWiM4ONh46aWXfHUJ9UZV13r69OlGQECA8c477xiHDx82Nm7caLRr18647777fHUJdd7Zs2eNvXv3Gnv37jUkGXPnzjX27t1rfP/994ZhGMaf/vQnY8yYMe76iq/dP/fcc8bXX39tLFiwgK/dXytef/1144YbbjCsVqtx2223Gbt27XLP3Xnnnca4ceM86t99912jffv2htVqNTp37mysW7euljuun6qyzhEREYakStv06dNrv/F6pqr/nn+JQHTlqrrOO3fuNKKiogybzWa0bdvW+M///E+jtLS0lruun6qy1iUlJUZycrLRrl07o1GjRkZ4eLjx+OOPG6dPn679xuuJLVu2XPD/byvWddy4ccadd95Z6TU9evQwrFar0bZtW2Pp0qU13qfFMLjHBwAAzI1niAAAgOkRiAAAgOkRiAAAgOkRiAAAgOkRiAAAgOkRiAAAgOkRiAAAgOkRiAAAgOkRiAAAgOkRiAAAgOkRiAAAgOkRiAAAgOn9f1Oi947O158SAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "y_rus.plot(kind = 'hist')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "2e028703-f049-4a2a-9539-e0c081a52bae",
   "metadata": {},
   "outputs": [],
   "source": [
    "#RANDDOM OVER SAMPLING\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "8f1fb825-5292-4466-8b67-fd784c17da6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from imblearn.over_sampling import RandomOverSampler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "d85a5deb-824c-486a-8b51-8ee86dfe1ae0",
   "metadata": {},
   "outputs": [],
   "source": [
    "ros = RandomOverSampler(random_state=2529)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "65e61178-2038-4e97-ba43-7ef975b43974",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_ros, y_ros = ros.fit_resample(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "164241fe-13d1-4d1d-b854-9f8a63ac7a86",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((15926, 10), (15926,), (10000, 10), (10000,))"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_ros.shape, y_ros.shape, x.shape, y.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "01ca7500-ebd8-4252-9b48-f15af74f5d0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Churn\n",
       "0    7963\n",
       "1    2037\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "fa242509-7c41-40a2-964b-6b8b97df5e9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='Frequency'>"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkQAAAGdCAYAAADzOWwgAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/TGe4hAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA1J0lEQVR4nO3dfXRU9Z3H8U8emBCQmQiYGVICRFEgiFqgwlSwi6REiK5KbKUgIEYpGlpJKk8rBQtqMAoIKqQqEjxCEXbRVSKBGARWiaCRKPIQUdBgwwS6kAyg5PHuH5zcZQQfMiSZhPt+nXPP6dzfd37zvb+q93Pu3LkJMgzDEAAAgIUFB7oBAACAQCMQAQAAyyMQAQAAyyMQAQAAyyMQAQAAyyMQAQAAyyMQAQAAyyMQAQAAywsNdAPNQU1NjYqLi9WmTRsFBQUFuh0AAPAzGIahEydOKCoqSsHBP34NiED0MxQXFys6OjrQbQAAAD8cOnRIHTt2/NEaAtHP0KZNG0lnFtRutwe4GwAA8HN4vV5FR0eb5/EfQyD6GWq/JrPb7QQiAACamZ9zuws3VQMAAMsjEAEAAMsjEAEAAMsjEAEAAMsjEAEAAMsjEAEAAMsjEAEAAMsjEAEAAMsLaCCqrq7WX//6V8XExCg8PFxXXHGF5syZI8MwzBrDMDRz5kx16NBB4eHhiouL0/79+33mOXbsmEaNGiW73a6IiAglJSXp5MmTPjWffvqpBg4cqJYtWyo6Olrp6emNcowAAKDpC2ggevLJJ7VkyRI999xz2rt3r5588kmlp6fr2WefNWvS09O1aNEiZWRkaPv27WrdurXi4+N1+vRps2bUqFHavXu3cnJytG7dOm3dulXjx483x71er4YMGaLOnTsrPz9fTz31lB599FG98MILjXq8AACgaQoyzr4c08huueUWOZ1OLV261NyXmJio8PBwvfrqqzIMQ1FRUfrLX/6ihx9+WJJUVlYmp9OpzMxMjRgxQnv37lVsbKw+/PBD9e3bV5KUnZ2tYcOG6ZtvvlFUVJSWLFmiRx55RB6PRzabTZI0bdo0vfHGG9q3b99P9un1euVwOFRWVsaf7gAAoJmoy/k7oFeIfv3rXys3N1eff/65JOmTTz7Re++9p6FDh0qSDh48KI/Ho7i4OPM9DodD/fr1U15eniQpLy9PERERZhiSpLi4OAUHB2v79u1mzY033miGIUmKj49XYWGhjh8/3uDHCQAAmraA/nHXadOmyev1qnv37goJCVF1dbUef/xxjRo1SpLk8XgkSU6n0+d9TqfTHPN4PIqMjPQZDw0NVdu2bX1qYmJizpmjduzSSy/1GSsvL1d5ebn52uv1XuihAgCAJiygV4hWr16tFStWaOXKlfr444+1fPlyPf3001q+fHkg21JaWpocDoe5RUdHB7QfAADQsAJ6hWjy5MmaNm2aRowYIUnq1auXvv76a6WlpWns2LFyuVySpJKSEnXo0MF8X0lJia677jpJksvl0pEjR3zmraqq0rFjx8z3u1wulZSU+NTUvq6tOdv06dOVmppqvvZ6vQ0airpMy2qwuRvKV3MTAt0CAOAHcF6pu4BeIfr2228VHOzbQkhIiGpqaiRJMTExcrlcys3NNce9Xq+2b98ut9stSXK73SotLVV+fr5Zs2nTJtXU1Khfv35mzdatW1VZWWnW5OTkqFu3bud8XSZJYWFhstvtPhsAALh4BTQQ3XrrrXr88ceVlZWlr776Sq+//rrmz5+vO+64Q5IUFBSkSZMm6bHHHtObb76pXbt2acyYMYqKitLtt98uSerRo4duvvlm3X///dqxY4fef/99TZw4USNGjFBUVJQkaeTIkbLZbEpKStLu3bv12muvaeHChT5XgQAAgHUF9CuzZ599Vn/961/14IMP6siRI4qKitIf//hHzZw506yZMmWKTp06pfHjx6u0tFQDBgxQdna2WrZsadasWLFCEydO1ODBgxUcHKzExEQtWrTIHHc4HNq4caOSk5PVp08ftW/fXjNnzvR5VhEAALCugD6HqLlo6OcQ8V0vAKA+cV45o9k8hwgAAKApIBABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLIxABAADLC2gg6tKli4KCgs7ZkpOTJUmnT59WcnKy2rVrp0suuUSJiYkqKSnxmaOoqEgJCQlq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+uk5+z/55BO1a9fugpsCAABoTH4Foj/84Q/685//rHfffVfV1dWqrq7Wpk2b9NBDD2nEiBH13SMAAECD8utXZnPmzNFXX32lwYMHKzT0zBQ1NTUaM2YM9xABAIBmx69AZLPZ9Nprr2nOnDn65JNPFB4erl69eqlz58713R8AAECD8ysQ1brqqqt01VVX1VcvAAAAAeFXIKqurlZmZqZyc3N15MgR1dTU+Ixv2rSpXpoDAABoDH4FooceekiZmZlKSEjQ1VdfraCgoPruCwAAoNH4FYhWrVql1atXa9iwYfXdDwAAQKPz62f3NptNXbt2re9eAAAAAsKvQPSXv/xFCxculGEY9d0PAABAo/PrK7P33ntP7777rtavX6+ePXuqRYsWPuNr166tl+YAAAAag1+BKCIiQnfccUd99wIAABAQfgWiZcuW1XcfAAAAAePXPUSSVFVVpXfeeUd///vfdeLECUlScXGxTp48WW/NAQAANAa/rhB9/fXXuvnmm1VUVKTy8nL99re/VZs2bfTkk0+qvLxcGRkZ9d0nAABAg/HrCtFDDz2kvn376vjx4woPDzf333HHHcrNza235gAAABqDX1eI/ud//kfbtm2TzWbz2d+lSxf985//rJfGAAAAGotfV4hqampUXV19zv5vvvlGbdq0ueCmAAAAGpNfgWjIkCF65plnzNdBQUE6efKkZs2axZ/zAAAAzY5fX5nNmzdP8fHxio2N1enTpzVy5Ejt379f7du31z/+8Y/67hEAAKBB+RWIOnbsqE8++USrVq3Sp59+qpMnTyopKUmjRo3yuckaAACgOfArEElSaGio7r777vrsBQAAICD8CkSvvPLKj46PGTPGr2YAAAACwa9A9NBDD/m8rqys1LfffiubzaZWrVoRiAAAQLPi16/Mjh8/7rOdPHlShYWFGjBggN83Vc+dO1dBQUGaNGmSue/06dNKTk5Wu3btdMkllygxMVElJSU+7ysqKlJCQoJatWqlyMhITZ48WVVVVT41mzdvVu/evRUWFqauXbsqMzPTrx4BAMDFye+/ZfZ9V155pebOnXvO1aOf48MPP9Tf//53XXPNNT77U1JS9NZbb2nNmjXasmWLiouLNXz4cHO8urpaCQkJqqio0LZt27R8+XJlZmZq5syZZs3BgweVkJCgQYMGqaCgQJMmTdJ9992nDRs2+H+wAADgolJvgUg6c6N1cXFxnd5z8uRJjRo1Si+++KIuvfRSc39ZWZmWLl2q+fPn66abblKfPn20bNkybdu2TR988IEkaePGjdqzZ49effVVXXfddRo6dKjmzJmj559/XhUVFZKkjIwMxcTEaN68eerRo4cmTpyoO++8UwsWLKi/AwcAAM2aX/cQvfnmmz6vDcPQ4cOH9dxzz+mGG26o01zJyclKSEhQXFycHnvsMXN/fn6+KisrFRcXZ+7r3r27OnXqpLy8PPXv3195eXnq1auXnE6nWRMfH68HHnhAu3fv1i9/+Uvl5eX5zFFbc/ZXc99XXl6u8vJy87XX663TMQEAgObFr0B0++23+7wOCgrSZZddpptuuknz5s372fOsWrVKH3/8sT788MNzxjwej2w2myIiInz2O51OeTwes+bsMFQ7Xjv2YzVer1fffffdeZ+blJaWpr/97W8/+zgAAEDz5lcgqqmpueAPPnTokB566CHl5OSoZcuWFzxffZo+fbpSU1PN116vV9HR0QHsCAAANKR6vYeoLvLz83XkyBH17t1boaGhCg0N1ZYtW7Ro0SKFhobK6XSqoqJCpaWlPu8rKSmRy+WSJLlcrnN+dVb7+qdq7Hb7Dz5VOywsTHa73WcDAAAXL7+uEJ199eSnzJ8//7z7Bw8erF27dvnsGzdunLp3766pU6cqOjpaLVq0UG5urhITEyVJhYWFKioqktvtliS53W49/vjjOnLkiCIjIyVJOTk5stvtio2NNWvefvttn8/Jyckx5wAAAPArEO3cuVM7d+5UZWWlunXrJkn6/PPPFRISot69e5t1QUFBPzhHmzZtdPXVV/vsa926tdq1a2fuT0pKUmpqqtq2bSu73a4//elPcrvd6t+/vyRpyJAhio2N1ejRo5Weni6Px6MZM2YoOTlZYWFhkqQJEyboueee05QpU3Tvvfdq06ZNWr16tbKysvw5dAAAcBHyKxDdeuutatOmjZYvX27+VP748eMaN26cBg4cqL/85S/10tyCBQsUHBysxMRElZeXKz4+XosXLzbHQ0JCtG7dOj3wwANyu91q3bq1xo4dq9mzZ5s1MTExysrKUkpKihYuXKiOHTvqpZdeUnx8fL30CAAAmr8gwzCMur7pF7/4hTZu3KiePXv67P/ss880ZMiQOj+LqKnzer1yOBwqKytrkPuJukxrflervpqbEOgWAAA/gPPKGXU5f/t1U7XX69XRo0fP2X/06FGdOHHCnykBAAACxq9AdMcdd2jcuHFau3atvvnmG33zzTf6r//6LyUlJfn8aQ0AAIDmwK97iDIyMvTwww9r5MiRqqysPDNRaKiSkpL01FNP1WuDAAAADc2vQNSqVSstXrxYTz31lL788ktJ0hVXXKHWrVvXa3MAAACN4YIezHj48GEdPnxYV155pVq3bi0/7s8GAAAIOL8C0f/+7/9q8ODBuuqqqzRs2DAdPnxY0pnnBtXXT+4BAAAai1+BKCUlRS1atFBRUZFatWpl7r/rrruUnZ1db80BAAA0Br/uIdq4caM2bNigjh07+uy/8sor9fXXX9dLYwAAAI3FrytEp06d8rkyVOvYsWPmn8wAAABoLvwKRAMHDtQrr7xivg4KClJNTY3S09M1aNCgemsOAACgMfj1lVl6eroGDx6sjz76SBUVFZoyZYp2796tY8eO6f3336/vHgEAABqUX1eIrr76an3++ecaMGCAbrvtNp06dUrDhw/Xzp07dcUVV9R3jwAAAA2qzleIKisrdfPNNysjI0OPPPJIQ/QEAADQqOp8hahFixb69NNPG6IXAACAgPDrK7O7775bS5cure9eAAAAAsKvm6qrqqr08ssv65133lGfPn3O+Rtm8+fPr5fmAAAAGkOdAtGBAwfUpUsXffbZZ+rdu7ck6fPPP/epCQoKqr/uAAAAGkGdAtGVV16pw4cP691335V05k91LFq0SE6ns0GaAwAAaAx1uofo+3/Nfv369Tp16lS9NgQAANDY/Lqputb3AxIAAEBzVKdAFBQUdM49QtwzBAAAmrs63UNkGIbuuece8w+4nj59WhMmTDjnV2Zr166tvw4BAAAaWJ0C0dixY31e33333fXaDAAAQCDUKRAtW7asofoAAAAImAu6qRoAAOBiQCACAACWRyACAACWRyACAACWRyACAACWRyACAACWRyACAACWRyACAACWRyACAACWF9BAtGTJEl1zzTWy2+2y2+1yu91av369OX769GklJyerXbt2uuSSS5SYmKiSkhKfOYqKipSQkKBWrVopMjJSkydPVlVVlU/N5s2b1bt3b4WFhalr167KzMxsjMMDAADNREADUceOHTV37lzl5+fro48+0k033aTbbrtNu3fvliSlpKTorbfe0po1a7Rl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+tOf5Ha71b9/f0nSkCFDFBsbq9GjRys9PV0ej0czZsxQcnKyeZVnwoQJeu655zRlyhTde++92rRpk1avXq2srOZ3Fz4AAKh/Ab1CtGTJEpWVlenf/u3f1KFDB3N77bXXzJoFCxbolltuUWJiom688Ua5XC6tXbvWHA8JCdG6desUEhIit9utu+++W2PGjNHs2bPNmpiYGGVlZSknJ0fXXnut5s2bp5deeknx8fGNerwAAKBpalLPIWqqeA7RuXgOEQA0XZxXzmi2zyECAAAIBAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwPAIRAACwvIAGoq1bt+rWW29VVFSUgoKC9MYbb/iMG4ahmTNnqkOHDgoPD1dcXJz279/vU3Ps2DGNGjVKdrtdERERSkpK0smTJ31qPv30Uw0cOFAtW7ZUdHS00tPTG/rQAABAMxLQQHTq1Clde+21ev755887np6erkWLFikjI0Pbt29X69atFR8fr9OnT5s1o0aN0u7du5WTk6N169Zp69atGj9+vDnu9Xo1ZMgQde7cWfn5+Xrqqaf06KOP6oUXXmjw4wMAAM1DaCA/fOjQoRo6dOh5xwzD0DPPPKMZM2botttukyS98sorcjqdeuONNzRixAjt3btX2dnZ+vDDD9W3b19J0rPPPqthw4bp6aefVlRUlFasWKGKigq9/PLLstls6tmzpwoKCjR//nyf4AQAAKyryd5DdPDgQXk8HsXFxZn7HA6H+vXrp7y8PElSXl6eIiIizDAkSXFxcQoODtb27dvNmhtvvFE2m82siY+PV2FhoY4fP37ezy4vL5fX6/XZAADAxavJBiKPxyNJcjqdPvudTqc55vF4FBkZ6TMeGhqqtm3b+tScb46zP+P70tLS5HA4zC06OvrCDwgAADRZTTYQBdL06dNVVlZmbocOHQp0SwAAoAE12UDkcrkkSSUlJT77S0pKzDGXy6UjR474jFdVVenYsWM+Neeb4+zP+L6wsDDZ7XafDQAAXLyabCCKiYmRy+VSbm6uuc/r9Wr79u1yu92SJLfbrdLSUuXn55s1mzZtUk1Njfr162fWbN26VZWVlWZNTk6OunXrpksvvbSRjgYAADRlAQ1EJ0+eVEFBgQoKCiSduZG6oKBARUVFCgoK0qRJk/TYY4/pzTff1K5duzRmzBhFRUXp9ttvlyT16NFDN998s+6//37t2LFD77//viZOnKgRI0YoKipKkjRy5EjZbDYlJSVp9+7deu2117Rw4UKlpqYG6KgBAEBTE9Cf3X/00UcaNGiQ+bo2pIwdO1aZmZmaMmWKTp06pfHjx6u0tFQDBgxQdna2WrZsab5nxYoVmjhxogYPHqzg4GAlJiZq0aJF5rjD4dDGjRuVnJysPn36qH379po5cyY/uQcAAKYgwzCMQDfR1Hm9XjkcDpWVlTXI/URdpmXV+5wN7au5CYFuAQDwAzivnFGX83eTvYcIAACgsRCIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5RGIAACA5VkqED3//PPq0qWLWrZsqX79+mnHjh2BbgkAADQBlglEr732mlJTUzVr1ix9/PHHuvbaaxUfH68jR44EujUAABBglglE8+fP1/33369x48YpNjZWGRkZatWqlV5++eVAtwYAAAIsNNANNIaKigrl5+dr+vTp5r7g4GDFxcUpLy/vnPry8nKVl5ebr8vKyiRJXq+3QfqrKf+2QeZtSA21FgCAC8d5xXdOwzB+stYSgehf//qXqqur5XQ6ffY7nU7t27fvnPq0tDT97W9/O2d/dHR0g/XY3DieCXQHAICLSUOeV06cOCGHw/GjNZYIRHU1ffp0paammq9ramp07NgxtWvXTkFBQfX6WV6vV9HR0Tp06JDsdnu9zo3/xzo3Dta5cbDOjYe1bhwNtc6GYejEiROKior6yVpLBKL27dsrJCREJSUlPvtLSkrkcrnOqQ8LC1NYWJjPvoiIiIZsUXa7nX/ZGgHr3DhY58bBOjce1rpxNMQ6/9SVoVqWuKnaZrOpT58+ys3NNffV1NQoNzdXbrc7gJ0BAICmwBJXiCQpNTVVY8eOVd++fXX99dfrmWee0alTpzRu3LhAtwYAAALMMoHorrvu0tGjRzVz5kx5PB5dd911ys7OPudG68YWFhamWbNmnfMVHeoX69w4WOfGwTo3Hta6cTSFdQ4yfs5v0QAAAC5ilriHCAAA4McQiAAAgOURiAAAgOURiAAAgOURiBrB888/ry5duqhly5bq16+fduzY8aP1a9asUffu3dWyZUv16tVLb7/9diN12rzVZZ1ffPFFDRw4UJdeeqkuvfRSxcXF/eT/Lzijrv8811q1apWCgoJ0++23N2yDF4m6rnNpaamSk5PVoUMHhYWF6aqrruK/HT9TXdf6mWeeUbdu3RQeHq7o6GilpKTo9OnTjdRt87N161bdeuutioqKUlBQkN54442ffM/mzZvVu3dvhYWFqWvXrsrMzGzwPmWgQa1atcqw2WzGyy+/bOzevdu4//77jYiICKOkpOS89e+//74REhJipKenG3v27DFmzJhhtGjRwti1a1cjd9681HWdR44caTz//PPGzp07jb179xr33HOP4XA4jG+++aaRO29e6rrOtQ4ePGj84he/MAYOHGjcdtttjdNsM1bXdS4vLzf69u1rDBs2zHjvvfeMgwcPGps3bzYKCgoaufPmp65rvWLFCiMsLMxYsWKFcfDgQWPDhg1Ghw4djJSUlEbuvPl4++23jUceecRYu3atIcl4/fXXf7T+wIEDRqtWrYzU1FRjz549xrPPPmuEhIQY2dnZDdongaiBXX/99UZycrL5urq62oiKijLS0tLOW//73//eSEhI8NnXr18/449//GOD9tnc1XWdv6+qqspo06aNsXz58oZq8aLgzzpXVVUZv/71r42XXnrJGDt2LIHoZ6jrOi9ZssS4/PLLjYqKisZq8aJR17VOTk42brrpJp99qampxg033NCgfV4sfk4gmjJlitGzZ0+ffXfddZcRHx/fgJ0ZBl+ZNaCKigrl5+crLi7O3BccHKy4uDjl5eWd9z15eXk+9ZIUHx//g/Xwb52/79tvv1VlZaXatm3bUG02e/6u8+zZsxUZGamkpKTGaLPZ82ed33zzTbndbiUnJ8vpdOrqq6/WE088oerq6sZqu1nyZ61//etfKz8/3/xa7cCBA3r77bc1bNiwRunZCgJ1HrTMk6oD4V//+peqq6vPeRq20+nUvn37zvsej8dz3nqPx9NgfTZ3/qzz902dOlVRUVHn/EuI/+fPOr/33ntaunSpCgoKGqHDi4M/63zgwAFt2rRJo0aN0ttvv60vvvhCDz74oCorKzVr1qzGaLtZ8metR44cqX/9618aMGCADMNQVVWVJkyYoP/4j/9ojJYt4YfOg16vV999953Cw8Mb5HO5QgTLmzt3rlatWqXXX39dLVu2DHQ7F40TJ05o9OjRevHFF9W+fftAt3NRq6mpUWRkpF544QX16dNHd911lx555BFlZGQEurWLzubNm/XEE09o8eLF+vjjj7V27VplZWVpzpw5gW4NF4grRA2offv2CgkJUUlJic/+kpISuVyu877H5XLVqR7+rXOtp59+WnPnztU777yja665piHbbPbqus5ffvmlvvrqK916663mvpqaGklSaGioCgsLdcUVVzRs082QP/88d+jQQS1atFBISIi5r0ePHvJ4PKqoqJDNZmvQnpsrf9b6r3/9q0aPHq377rtPktSrVy+dOnVK48eP1yOPPKLgYK4zXKgfOg/a7fYGuzokcYWoQdlsNvXp00e5ubnmvpqaGuXm5srtdp/3PW6326deknJycn6wHv6tsySlp6drzpw5ys7OVt++fRuj1WatruvcvXt37dq1SwUFBeb27//+7xo0aJAKCgoUHR3dmO03G/7883zDDTfoiy++MAOnJH3++efq0KEDYehH+LPW33777TmhpzaIGvxp0HoRsPNgg96yDWPVqlVGWFiYkZmZaezZs8cYP368ERERYXg8HsMwDGP06NHGtGnTzPr333/fCA0NNZ5++mlj7969xqxZs/jZ/c9Q13WeO3euYbPZjP/8z/80Dh8+bG4nTpwI1CE0C3Vd5+/jV2Y/T13XuaioyGjTpo0xceJEo7Cw0Fi3bp0RGRlpPPbYY4E6hGajrms9a9Yso02bNsY//vEP48CBA8bGjRuNK664wvj9738fqENo8k6cOGHs3LnT2LlzpyHJmD9/vrFz507j66+/NgzDMKZNm2aMHj3arK/92f3kyZONvXv3Gs8//zw/u79YPPvss0anTp0Mm81mXH/99cYHH3xgjv3mN78xxo4d61O/evVq46qrrjJsNpvRs2dPIysrq5E7bp7qss6dO3c2JJ2zzZo1q/Ebb2bq+s/z2QhEP19d13nbtm1Gv379jLCwMOPyyy83Hn/8caOqqqqRu26e6rLWlZWVxqOPPmpcccUVRsuWLY3o6GjjwQcfNI4fP974jTcT77777nn/e1u7rmPHjjV+85vfnPOe6667zrDZbMbll19uLFu2rMH7DDIMrvEBAABr4x4iAABgeQQiAABgeQQiAABgeQQiAABgeQQiAABgeQQiAABgeQQiAABgeQQiAABgeQQiAABgeQQiAABgeQQiAABgeQQiAABgef8H7TFTPiSuL/IAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "y_ros.plot(kind = 'hist')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "f74665a3-594a-47c5-bb39-b53aa4a1e8c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#TRAIN TEST SPLIT"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "c3ed8700-238b-4bc4-9577-fd8ed3ca19bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "6cd762d7-7e5f-416b-8764-3f3118f75b28",
   "metadata": {},
   "outputs": [],
   "source": [
    "#SPLIT ORIGINAL DATA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "26608113-c6d8-4bfc-9758-8ba5f0fe2a28",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "799f5895-45f1-42d4-b690-336d2f879ea4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#MODEL ACCURACY\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "85c4217d-9940-4ae7-8168-3852e20c7007",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix, classification_report"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "91337d80-7c05-42e5-a2f3-844ff0881946",
   "metadata": {},
   "outputs": [],
   "source": [
    "#HYPEPARAMETER TUNNING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "caaf48f6-1b1e-42db-8768-709a872321b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1164204e-e5d1-45c6-9f5a-eeab72046064",
   "metadata": {},
   "outputs": [],
   "source": [
    "param_grid = {'c': [0.1,1, 10],\n",
    "              'gramma':[1,0.1,0.01],\n",
    "              'kernel': ['rbf'],\n",
    "              'class-weight':['balanced']}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d48cde6-61fe-4155-87d1-d040b63cf70a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

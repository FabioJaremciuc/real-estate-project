import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# it is necessary to change the file path
df = pd.read_csv('/home/jaremciuc/data_analysis_test/assignment_data.csv')

# call the functions presents in the real-estate-table.py 
remove_nan()
create_plot()
create_apartment()
create_house()
types_clean()
create_locations()
concat_clean()
create_features()

# Analyzing apartments in Golden Mile
golden = df[df['locations']=='Golden Mile']
goldenap = golden[golden['type']=='apartment']

# apartments in Golden Mile with Swimming pool
goldenap_p = goldenap[(goldenap['pool']=='1') & (goldenap['garage']=='0') & (goldenap['sea view']=='0')].copy()

# Creates price column by square meters
goldenap_p['total_area'] = goldenap_p['total_area'].astype(int).copy()
goldenap_p['m_qdr'] = ((goldenap_p['price'] / df['total_area']))

plt.scatter(goldenap_p['total_area'], goldenap_p['price'], s=20, c=goldenap_p['m_qdr'])
plt.title("prices of apartments with swimming pool in m_sqtr")
plt.xlabel("m_sqtr")
plt.ylabel("Prices")
plt.show()

# Apartments in Golden Mile with garage
goldenap_g = goldenap[(goldenap['pool']=='0') & (goldenap['garage']=='1') & (goldenap['sea view']=='0')].copy()

# Creates price column by square meters
goldenap_g['total_area'] = goldenap_g['total_area'].astype(int)
goldenap_g['m_qdr'] = ((goldenap_g['price'] / df['total_area']))

plt.scatter(goldenap_g['total_area'], goldenap_g['price'], s=20, c=goldenap_g['m_qdr'])
plt.title("prices of apartments with garage in m_sqtr")
plt.xlabel("m_sqtr")
plt.ylabel("Prices")
plt.show()

# Apartments in Golden Mile with sea view 
goldenap_g = goldenap[(goldenap['pool']=='0') & (goldenap['garage']=='0') & (goldenap['sea view']=='1')].copy()

# Creates price column by square meters
goldenap_g['total_area'] = goldenap_g['total_area'].astype(int)
goldenap_g['m_qdr'] = ((goldenap_g['price'] / df['total_area']))

plt.scatter(goldenap_g['total_area'], goldenap_g['price'], s=20, c=goldenap_g['m_qdr'])
plt.title("prices of apartments with sea view and pool in m_sqtr")
plt.xlabel("m_sqtr")
plt.ylabel("Prices")
plt.show()

# Apartments in Golden Mile with swimming pool and garage
goldenap_p = goldenap[(goldenap['pool']=='1') & (goldenap['garage']=='1') & (goldenap['sea view']=='0')].copy()

# Creates price column by square meters
goldenap_p['total_area'] = goldenap_p['total_area'].astype(int).copy()
goldenap_p['m_qdr'] = ((goldenap_p['price'] / df['total_area']))

plt.scatter(goldenap_p['total_area'], goldenap_p['price'], s=20, c=goldenap_p['m_qdr'])
plt.title("prices of apartments with pool and garage in m_sqtr")
plt.xlabel("m_sqtr")
plt.ylabel("Prices")
plt.show()

# Apartments in Golden Mile with garage and sea view
goldenap_g = goldenap[(goldenap['pool']=='0') & (goldenap['garage']=='1') & (goldenap['sea view']=='1')].copy()

# Creates price column by square meters
goldenap_g['total_area'] = goldenap_g['total_area'].astype(int)
goldenap_g['m_qdr'] = ((goldenap_g['price'] / df['total_area']))

plt.scatter(goldenap_g['total_area'], goldenap_g['price'], s=20, c=goldenap_g['m_qdr'])
plt.title("prices of apartments with garage and sea view in m_sqtr")
plt.xlabel("m_sqtr")
plt.ylabel("Prices")
plt.show()

# Apartments in Golden Mile with swimming pool and sea view
goldenap_g = goldenap[(goldenap['pool']=='1') & (goldenap['garage']=='0') & (goldenap['sea view']=='1')].copy()

# Creates price column by square meters
goldenap_g['total_area'] = goldenap_g['total_area'].astype(int)
goldenap_g['m_qdr'] = ((goldenap_g['price'] / df['total_area']))

plt.scatter(goldenap_g['total_area'], goldenap_g['price'], s=20, c=goldenap_g['m_qdr'])
plt.title("prices of apartments with sea view and pool pool in m_sqtr")
plt.xlabel("m_sqtr")
plt.ylabel("Prices")
plt.show()

# Apartments in Golden Mile without swimming pool, sea view and garage
goldenap_g = goldenap[(goldenap['pool']=='0') & (goldenap['garage']=='0') & (goldenap['sea view']=='0')].copy()

# Creates price column by square meters
goldenap_g['total_area'] = goldenap_g['total_area'].astype(int)
goldenap_g['m_qdr'] = ((goldenap_g['price'] / df['total_area']))

plt.scatter(goldenap_g['total_area'], goldenap_g['price'], s=20, c=goldenap_g['m_qdr'])
plt.title("prices of apartments without sea view, pool and garage in m_sqtr")
plt.xlabel("m_sqtr")
plt.ylabel("Prices")
plt.show()




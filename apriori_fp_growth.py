import pandas as pd
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Load dataset
file_path = "final_dataset_ready_superclean.csv"  # ✅ Use the new file
df = pd.read_csv(file_path)

# Group products by each user
transactions = df.groupby('user_id')['product_name'].apply(list).tolist()

# Encode the transactions into one-hot matrix
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

print(f"✅ Transactions created: {len(transactions)} users, {len(df_encoded.columns)} unique products.")

# Train Apriori Algorithm
try:
    print("🔵 Running Apriori...")
    frequent_itemsets_apriori = apriori(df_encoded, min_support=0.005, use_colnames=True, verbose=1)
    rules_apriori = association_rules(frequent_itemsets_apriori, metric="confidence", min_threshold=0.3)
    rules_apriori.to_csv("apriori_rules.csv", index=False)
    print(f"✅ Apriori rules generated: {len(rules_apriori)} rules.")
except Exception as e:
    print(f"❌ Apriori Error: {e}")

# Train FP-Growth Algorithm
try:
    print("🔵 Running FP-Growth...")
    frequent_itemsets_fpgrowth = fpgrowth(df_encoded, min_support=0.005, use_colnames=True)
    rules_fpgrowth = association_rules(frequent_itemsets_fpgrowth, metric="confidence", min_threshold=0.3)
    rules_fpgrowth.to_csv("fpgrowth_rules.csv", index=False)
    print(f"✅ FP-Growth rules generated: {len(rules_fpgrowth)} rules.")
except Exception as e:
    print(f"❌ FP-Growth Error: {e}")

print("\n✅✅ Rules generation completed successfully based on PRODUCTS!")

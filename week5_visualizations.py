# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# reading the dataset
df = pd.read_csv("mushrooms.csv")
# print(df.head())

# bar plot between count of edible and poisonus mushrooms
class_counts = df["class"].value_counts()

fig, ax = plt.subplots()
# creating a bar chart
ax.bar(class_counts.index, class_counts.values)

# adding title and axis labels
ax.set_title("Count of Edible vs Poisonous Mushrooms")
ax.set_xlabel("Class")
ax.set_ylabel("Count")

# saving the ploat
plt.savefig("output/class_distribution.png")
plt.show()

# plot between odor and class

# plot grouped bar chart
odor_class = df.groupby(["odor", "class"]).size().unstack()
fig, ax = plt.subplots()
odor_class.plot(kind="bar", ax=ax)

# adding title and axis labels
ax.set_title("Mushroom Odor vs Class")
ax.set_xlabel("Odor Type")
ax.set_ylabel("Count")

# saving the ploat
plt.savefig("output/odor_vs_class.png")
plt.show()


# plot for cap color distribution
cap_counts = df["cap-color"].value_counts()
fig, ax = plt.subplots()

# creating a bar graph
ax.bar(cap_counts.index, cap_counts.values)

# adding title and axis labels
ax.set_title("Distribution of Cap Colors")
ax.set_xlabel("Cap Color")
ax.set_ylabel("Count")
# saving the ploat
plt.savefig("output/cap_color.png")
plt.show()

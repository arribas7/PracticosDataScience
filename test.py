 [
    "data = np.array(largos)\n",
    "print (data)\n",
    "# hagamos lo mismo:\n",
    "unique, counts = np.unique(data, return_counts=True)\n",
    "sns.barplot(unique, counts/counts.sum())"
   ]
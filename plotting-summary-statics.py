# Next plot the statics

# Why we're using the statics here

# We're using the statics to plot the data in the form of the graph

# value_counts() return the counting of the unique value.
# What this line is doing?
# This line counting the value in the coloumn final grade & sort the indexing
grade_counts = final_data["Final Grade"].value_counts().sort_index()

# What this line is doing?
# This line is plotting the graph in the form of the bar()
grade_counts.plot.bar()

# we need to show the graph
# Why this line has used?
# This line has used to show the graph because it's only a script
plt.show()

# Next we're gonna see the histogram
# We'll use the bins. The bins show the interval between the plot

final_data["Final Score"].plot.hist(bins = 20, label = "Histogram")


# Let's get the density estimation

final_data["Final Score"].plot.density(linewidth = 4, label = "Kernel Density Estimate")

# Finding the mean of the plot


final_mean = final_data["Final Score"].mean()

#Standard deviation is used to find the how many far the value from
# the mean value

final_std = final_data["Final Score"].std()

# What's the use of the linspace() method
# The linspace() method is used to give the evenly space in the specified
# Interval. Here we're using the linspace to generate the value
# from the -5 to +5.

x = np.linsopace(final_mean - 5*final_std, final_mean + 5* final_std)

# We'll plot the normal distribution
# Normal distribution is used to get the near value from the mean
# We use normal distribution to find the value above or low through the
# mean value

normal_dist = scipy.stats.norm.pdf(x,loc = final_mean,scale = final_std)

# let's plot the normal distribution
plt.plot(x, normal_dist, label="Normal Distribution", linewidth=4)

# legend() function is used to specify the area covered by the elements

plt.legend()

# We need to show the graph outside the script. Hence, I'm going to use the
# show() method
plt.show()












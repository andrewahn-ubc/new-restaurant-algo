


# INPUT: the dataframe containing all restaurant ratings for every user ("df"), 
#        a list of users ("interestedUsers") for whom we want to recommend restaurants they've never been to before,
# OUTPUT: an array of restaurants 

# PSEUDOCODE
# copy "df" into a new variable, "dfWithPredictions", since it's prob good to keep a "pure" version
#
# for each interestedUser in "interestedUsers", 
#   
#   initialize an array ("simScore") containing interestedUser's similarity score with every other user in "dfWithPredictions"
#   
#   for every other user ("otherUser") in "dfWithPredictions",
#       compute cosine_similarity(interestedUser, otherUser) and push to "simScore" (runTime)
#
#   for every restaurant ("restaurant") in "dfWithPredictions",
#       take the dot of "simScore" and "resaurant"s ratings, then divide this number by the sum of "simScores"






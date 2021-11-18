#INFO CORNER

## Model evaluation

### Evaluating recommender systems

To ascertain how reliable our models are we need to determine the quality of the predictions that they make. To do that in Python we can use scikit-learn's metrics module. Within this module you can find all sorts of functions for scoring your models and evaluating their predictive performance. Use these results to help you select the best model for your given situation. 

#### Precision
Precision = Number of items that I like that were also recommended to me / Number of items recommended

The first metric we'll look at is precision. Precision is a measure of a model's relevancy. To represent it algebraically, you can think of precision as the number of items that I liked that were also recommended to me divided by the number of items that were recommended to me. Or, in other words, how relevant were the recommendations that were made? So, for example, if a system recommended eight items and four of those items were items that you like, then the system would have achieved 50% precision. 

#### Recall
Recall = Number of items that I liked that were also recommended to me / Number of items that I liked   

Another important metric is recall. Recall is a measure of the model's completeness. To represent it algebraically you can think of recall as equal to the number of items that I liked that were also recommended to me divided by the number of items that I liked. In other words, how completely did the recommender system predict the items that I liked? As an example, if a system recommended eight out of ten items that you liked, then the system would have achieved 80% completion or 80% recall. 


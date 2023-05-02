# mvp
## Predicting the MVP of the NBA

The aim of this project is to forecast the most valuable player of this NBA season using the data of the last ten years' stats and voting results.
It is written in Python using basketball-reference data, pre-processing with Pandas, predicting models with Scikit-learn and building a [web-app](https://michalissak-mvp-streamlit-app-aqocmg.streamlit.app/) with Streamlit for the presentation.

## Procedure
The top 10 players were selected based on their [probability](https://www.basketball-reference.com/friv/mvp.html) from basketball-reference to win this year's MVP. A dataframe was created containing their team wins, per 36 minutes, totals, and advanced stats. The same process was then repeated for the past 10 years' voting results, with the addition of a column displaying their voting share. The data was normalized and fed into a list of predictive models, using different lists of features to compare the results. Ultimately, a web-app was developed to display the findings.
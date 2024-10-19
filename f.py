#Create a Dictionary with 10 key value pairs. Now convert this Dictionary to Dataframe using Pandas.
import pandas as pd
dict1={
    "name":['harry','pawan','ayush','rachit','ankit','satyam','anshu','tauhid','raj','shobhit'],
    "marks":[34,67,56,65,44,61,41,49,57,51],
    "city":['rampur','kolkata','delhi','gujarat','allahabad','mumbai','chennai','lucknow','ghaziabad','jaipur']
}
df=pd.DataFrame(dict1)

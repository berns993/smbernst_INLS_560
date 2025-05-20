#From the Sample Code, "Future Value": https://lawrencejones-lblakej.cloudapps.unc.edu/inls-560/code/02/02_18_%20future_value
# Get the desired future value.

future_value = 600
rate = 2.0
years = 10
present_value = future_value / (1.0 + rate)**years

print('You will need to deposit this amount:', present_value)
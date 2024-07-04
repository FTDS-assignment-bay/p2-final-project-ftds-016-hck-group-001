import streamlit as st

def app():
    st.title('Exploratory Data Analysis')
    
    st.header('Total Complaints by Product')
    st.image('./images/1. Complaint by Products.png')
    st.write("The product that received the most complaints from consumers was `Debt Collection` with 2,064 complaints, then `Payday Loan` with 82 complaints and finally `Student Loan` with 75 complaints.")
    st.divider()
    
    st.header('Total Complaints by Sub Products')
    st.image('./images/2. Complaints by Sub Products.png')
    st.write("There are 10 Sub Products that receive complaints from consumers and the most in `Other (i.e. phone, health club, etc.)` as many as 737 complaints while the Sub Products that received the least complaints on `Federal Student Loan Service` were 20 complaints.")
    st.divider()
    
    st.header('Issue Distribution')
    st.image('./images/3. Issue Distribution.png')
    st.write("There are 16 main consumer problems and the most common problem is `Cont'd attempts collect debt not owed` with 1,025 complaints, then `Communication tactis` as many as 285 complaints, `Diclosure verification of debt` as many as 279 complaints and the main consumer problem which is `Charged bank acc wrong day or amt` as many as 4 complaints. ")
    st.divider()
    
    st.header('Sub Issue Distribution')
    st.image('./images/4. Sub Issue Distribution.png')
    st.write("Out of 44 sub-issues faced by consumers, there are 10 sub-issues that are most frequently encountered. `Debt is not mine` is the most common sub-issue faced by consumers, with 616 complaints. In the 10th position is `Threatened to sue on too old debt`, with 40 complaints.")
    st.divider()
    
    st.header('Complaints by State')
    st.image('./images/5. Complaints by State.png')
    st.write("There are 55 States in the United States, there are 10 states that file the most complaints, including:")
    st.write("- California **(CA)** is the State with the most complaints with 279 complaints. ")
    st.write("- Texas **(TX)** is the second most filed with 226 complaints.") 
    st.write("- Florida **(FL)** is the third place with the most complaints with 177 complaints.")
    st.write("- Washington **(WA)** is the tenth position with the most complaints with 62 complaints.")
    st.divider()
    
    st.header('Complaints by Company')
    st.image('./images/6. Complaints by Company.png')
    st.write("Among the 556 companies involved, there are 10 companies that received the most complaints from consumers. These are:")
    st.write("- `ERC` is the company with the highest number of complaints, totaling 118 complaints.")
    st.write("- The second company with the most complaints is `Citibank`, with 72 complaints.")
    st.write("- The third company with the most complaints is `Bank of America`, with 55 complaints.")
    st.write("- The tenth company with the most complaints is `Wells Fargo & Company`, with 45 complaints.")
    st.divider()
    
    st.header('Company Responses to Consumers')
    st.image('./images/7. Company Responses to Consumers.png')
    st.write("There are 4 categories of responses given by the Company:")      
    st.write("- **Closed with Explanation:** This is the most common type of response, with 1,751 instances. It indicates that the majority of complaints were resolved by providing an explanation to the consumer.")
    st.write("- **Closed with non-monetary relief:** The second most common response type, with 324 instances. This implies that the company provided some form of relief or resolution that did not involve monetary compensation.")
    st.write("- **Closed:** There are 115 instances of complaints being simply closed without additional context provided. This might indicate cases where no further action was necessary or possible.")
    st.write("- **Closed with monetary relief:** There were 31 responses from companies that were closed with monetary compensation. This suggests that in only a small number of cases did the companies provide monetary compensation as part of the resolution.")
    st.divider()
    
    st.header('Distribution of Timely Response')
    st.image('./images/8. Distribution of Timely Response.png')
    st.write("The chart indicates that most companies are very efficient in responding to consumer complaints in a timely manner, with 95.7% of complaints receiving timely responses. However, there is still room for improvement to ensure that all complaints are handled promptly, as 4.3% of complaints did not receive timely responses. Timely handling of complaints is crucial for consumer satisfaction and maintaining the company's reputation.")
    st.divider()
    
    st.header('Complaints Received Each Month and Yea')
    st.image('./images/9. Complaints Received Each Month and Year.png')
    st.write("The number of complaints received each month in 2015 and 2016 fluctuated.")
    st.write("- In 2015, 70 complaints were received in March and an increase of 140 complaints in September. ")
    st.write("- In 2016, 88 complaints were received starting in January and there was an increase of 165 complaints in March, marking the highest peak for 2016. The significant decline began in September, with the number of complaints gradually decreasing to below 20 complaints in November.")
    st.divider()
    
    st.header('Comparison of Complaint Trends Received vs Sent to Company')
    st.image('./images/10. Comparison of Complaint Trends Received vs Sent to Company.png')
    st.write(" - There are noticeable peaks in complaints around March 2016 for both date types.")
    st.write("- The absence of significant differences between the number of complaints received and sent to the company suggests that complaints are processed without delays. This highlights the promptness of the complaint management process.")
    st.write("- Both lines peak at approximately the same points, such as in March 2016, suggesting synchronous handling of complaints.")
    st.write("- Complaints generally rise and fall together in both 2015 and 2016, with significant peaks in the middle of the year and declines towards the end of the year.")
    st.write("- The sharp decline in complaints after August 2016 is evident in both lines.")
    st.divider()
    
    st.header('Proportion of Complaints category')
    st.image('./images/eda_labeled_1.png')
    st.write("Most complaints are mild, mild-harsh, or mild-light")
    st.write("- There are cases where complaints are both light and harsh at the same time, or even light-mild-harsh")
    st.divider()
    
    st.header('Average Response Time of Each Complaints Category')
    st.image('./images/eda_labeled_2.png')
    st.write("The likelihood of getting harsh complaints increases as response time increases.")
    st.divider()
    
    st.header('Products Ranking by Harsh Complaints Probability')
    st.image('./images/eda_labeled_3.png')
    st.write("The ranking of products by harsh complaints' probability is Debt Collection, Payday Loan Product, Student Loan.")
    st.divider()
    
    st.header('Issues Ranking by Harsh Complaints Porbability')
    st.image('./images/eda_labeled_4.png')
    st.write("The top 5 issues with the highest harsh complaints' probability are:") 
    st.write("- Payment to acct not credited")
    st.write("- Charged bank acct wrong day or amt")
    st.write("- Disclosure verification of debt")
    st.write("- Taking/threatening an illegal action")
    st.write("- Cont'd attempts collect debt not allowed")
    st.divider()
    
    st.header('Common Words in Light & Harsh Complaints')
    st.image('./images/eda_labeled_5.png')
    st.write("Some words that stand out are:")
    st.write("- Light: please, thank, help")
    st.write("- Harsh: theft, illegal, threatening")
    st.divider()
    
if __name__ == '__main__':
    app()
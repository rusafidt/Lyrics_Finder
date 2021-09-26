import requests
url1="https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=83b03ae524ae432c8c6d71bab1967b1e&query="
movie1=input("Enter The  movie You Love:")
movie2=" "
z3=" "
z4=" "
z5=" "
z6=" "
z7=" "
z8=" "
z2=" "
z9=" "
z10=" "
r=" " 
movie3=movie1.lower()
for i in movie3:
    if(i==" "):
        movie2=movie2+'%20'
    else:
        movie2=movie2+i
url1=url1+movie2
z=json_wadu=requests.get(url1).json()
z2=json_wadu['results'][0]['display_title']
print(z2)
z3=json_wadu['results'][0]['headline']
print(z3)
z4=json_wadu['results'][0]['summary_short']
print(z4)
z5=json_wadu['results'][0]['mpaa_rating']
print("It's official mpaa rating is : ",z5)
z6=json_wadu['results'][0]['byline']
print("By : ", z6)
z7=json_wadu['results'][0]['publication_date']
print("The publication date was on : ",z7)
z8=json_wadu['results'][0]['opening_date']
print("The opening date was on : ",z8)
z9=json_wadu['results'][0]['link']
print (z9['suggested_link_text'] , " : ", z9['url'])
z10=json_wadu['copyright']
print(z10)




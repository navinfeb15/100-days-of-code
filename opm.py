import requests


for page in range(1,100):
  response = requests.get(f"https://cdn.hxmanga.com/file/majekayoo/onepunch-man/Chapter-183/{page:02}.jpg")
  if response.status_code == 200 and page == 7:
      with open(f"./opm/{page}.jpg", 'wb+') as f:
          f.write(response.content)
          print(f"downloaded {page} page...\n")
  else:
    print(f"ended at page {page}")
    break
    
  
    
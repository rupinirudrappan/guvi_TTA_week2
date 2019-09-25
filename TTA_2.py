employ_dict = [{"name":"ramesh","age":25, "dept":"engineering","designation":"DB Engineer","salary":30000},
                 {"name":"leena","age":23, "dept":"engineering","designation":"Architect","salary":80000},
                 {"name":"sherlock","age":30, "dept":"sales","designation":"Sales Officer","salary":60000},
                 {"name":"lestrade","age":40, "dept":"sales","designation":"VP","salary":100000},
                 {"name":"bean","age":35, "dept":"support","designation":"VP","salary":200000},
                 {"name":"stapleton","age":20, "dept":"hr",'designation':"Intern","salary":5000}]
for x in employ_dict:
    if x['designation']!="Intern":
        if x['designation']=="VP":
            x['salary']+=(25/100)*x['salary']
        elif x['dept']=="engineering":
            x['salary']+=(15/100)*x['salary']
        elif x['dept']=="sales":
            x['salary']+=(10/100)*x['salary']
        elif x['dept']=="support":
            x['salary']+=(12.5/100)*x['salary']
for x in employ_dict:
    print(x['name'],x['salary'])
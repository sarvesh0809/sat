from django.shortcuts import render,HttpResponse
from googletrans import Translator
import xlrd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Create your views here.
results=[]
scatter_y=[]
lis=[]
scatter_x=[]
def home(request):

    if request.method =="POST":
        if 'myFile' in request.FILES: 
            file = request.FILES["myFile"]

            ext = file.name.split('.')[-1]
            if ext == "xlsx":
                translator = Translator()
                wb = xlrd.open_workbook(file_contents=file.read())
                sheet = wb.sheet_by_index(0)
                num_rows = sheet.nrows
                global scatter_x
                scatter_x=[]
                global scatter_y
                scatter_y = []
                global results
                results =[]
                x_axis = ["negative", "neutral", "positive"]
                y_axis = [0, 0, 0]                
                for i in range(0, num_rows):
                    sentence = sheet.cell_value(i, 0)
                    translations = translator.translate(sentence, dest='en')
                    trans_text = translations.text
                    results.append(sentence)
                    # print(trans_text)
                    analyser = SentimentIntensityAnalyzer()
                    result = analyser.polarity_scores(trans_text)
                    
                    # print(result)

                    if(result["compound"] < 0):
                        y_axis[0] += 1
                        scatter_x.append(result["compound"])
                        scatter_y.append("negative")

                    if(result["compound"] == 0):
                        y_axis[1] += 1
                        scatter_x.append(result["compound"])
                        scatter_y.append("neutral")

                    if(result["compound"] > 0):
                        y_axis[2] += 1
                        scatter_x.append(result["compound"])
                        scatter_y.append("positive")

                global lis    
                lis=[]
                count = 0
                for items in scatter_x:
                    count += 1
                    lis.append(count)
                    
                    

                lst = [{'item1': t[0], 'item2': t[1], 'item3': t[2], 'item4': t[3]} for t in zip(lis, scatter_x,scatter_y,results)]
                # context={
                #     "lst":lst
                # }
                return render(request, "index.html", {"something": True, "scatter_x": scatter_x, "lis": lis, "x_axis": x_axis, "y_axis": y_axis,"lst":lst})
            else:
                return render(request,"base.html")

        else:
            return  render(request,"base.html")
    else:
        return render(request, "index.html")
    return lis,scatter_x,scatter_y,results



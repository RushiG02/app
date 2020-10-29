from flask import Flask,request
import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("gunjal0200@gmail.com","im@gunjal")
menu={
    'sandwich':40,
    'cheese sandwich':40,
    'grilled cheese sandwich':50,
    'Egg Sandwich':55,
    'salad':70,
    'pasta':60,
    'chiken soup':150,
    "chiken tikka":130,
    'Dosa':60,
    'biryani':120,
    'chiken dumpling':100,
    'pizza':200,
    'mango lassi':20
}
app=Flask(__name__)
@app.route("/")
def home():
    return 'Home'
@app.route("/jsonprocess",methods=['POST'])
def json_process():
    data=request.get_json()
    i=data['queryResult']['parameters']['food_items_entity']
    q=data['queryResult']['parameters']['number']
    amount=0
    for x in range(len(q)):
        item=i[x]
        amount+=menu[str(item)]*q[x]
    msg='order recived for  '
    for x in range(len(i)):
            msg += str(q[x]) + ' - ' + str(i[x])+', '
    subject='order confirmation'
    server.sendmail("gunjal0200@gmail.com", "gunjalrs32@gmail.com", '''subject:{}\n{}
    and your final amount is {}INR'''.format(subject,msg,amount))
    server.quit()
    return '''{}
            and your final amount is {}INR'''.format(msg,amount)

if __name__=='__main__':
    app.run(debug=True)
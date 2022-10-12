#1 - Define a dictionary call story1, it should have the followign keys:
        # 'start', 'middle' and 'end'
story1={ "start":"A. P. J. Abdul Kalam was an Indian aerospace scientist and statesman who served as the 11th President of India from 2002 to 2007.He was born and raised in Rameswaram, Tamil Nadu and studied physics and aerospace engineering.He is known as Missile Man of India.",
        "middle" :"Kalam was elected as the 11th president of India in 2002.Widely referred to as the \"People's President\".He was a recipient of several prestigious awards, including the Bharat Ratna, India's highest civilian honour",
         "end" : "While delivering a lecture at the Indian Institute of Management Shillong, Kalam collapsed and died from an apparent cardiac arrest on 27 July 2015, aged 83" }
#2 - Print the entire dictionary
print(story1)
#3 - Print the type of your dictionary
print(type(story1))
#4 - Print only the keys
print(story1.keys())
#5 - print only the values
print(story1.values())
#6 - print the individual values using the keys (individually, lots of printi commands)
print(story1["start"])
print(story1["middle"])
print(story1["end"])
#7 - Now let's add a new key:value pair.
# 'hero': yourSuperHero
story1["hero"]="A.P.J Abdul Kalam"

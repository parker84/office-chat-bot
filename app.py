from email.policy import default
import os
from decouple import config
import openai
import streamlit as st

openai.api_key = config("OPENAI_API_KEY")

st.set_page_config(
    page_icon='🏢',
    page_title='Office Chatbot',
    menu_items={
        'Get Help': 'https://join.slack.com/t/officechatbot/shared_invite/zt-14rlr8chh-C~rwJN~~KUAX~DOkvcno1g',
        'Report a bug': "https://github.com/parker84/office-chat-bot/issues/new",
        'About': "This dashboard was initially created by [Brydon Parker](https://linkpop.com/brydon)."
    }
)
st.title("🏢 Dunder Mifflin Rabies Awareness Chatbot For the Cure")

st.sidebar.title("🏢 The Office Chatbot")
st.sidebar.markdown("""

**Feedback/Questions**: 
[join our slack workspace](https://join.slack.com/t/officechatbot/shared_invite/zt-14rlr8chh-C~rwJN~~KUAX~DOkvcno1g)

Like 🏢 **The Office Chatbot** and want to say thanks? [:coffee: buy me a coffee](https://www.buymeacoffee.com/brydon)
""")


jim_line = st.text_input("Say something to Dwight Schrute:", value='bears beats battlestar gallactica')

def dwight_and_jim_prompt(jim_line):
    return f"""Predict what Dwight will say next

Dwight Schrute: Whenever I'm about to do something, I think 'Would an idiot do that?' And if they would, I do not do that thing.
Dwight Schrute: Who is Justice Beaver?
Dwight Schrute: I love catching people in the act. That's why I always whip open doors.
Dwight Schrute: R' is among the most menacing of sounds. That's why they call it 'murder' and not 'mukduk'
Dwight Schrute: When someone smiles at me, all I see is a chimpanzee begging for its life.
Dwight Schrute: You better learn your rules. If you don't, you'll be eaten in your sleep.
Dwight Schrute: Why are all these people here? There's too many people on this earth. We need a new plague.
Dwight Schrute: In the end, the greatest snowball isn't a snowball at all. It's fear. Merry Christmas.
Dwight Schrute: All you need is love. False. The four basic human necessities are air, water, food, and shelter.
Dwight Schrute: I am ready to face any challenge that might be foolish enough to face me.
Dwight Schrute: To avoid illness, expose yourself to germs, enabling your immune system to develop antibodies. I don't know why everyone doesn't do this... Maybe they have something against living forever.
Dwight Schrute: In an ideal world I would have all ten fingers on my left hand and the right one would just be left for punching.
Dwight Schrute: Security in this office park is a joke. Last year I came to work with my spud-gun in a duffel bag. I sat at my desk all day with a rifle that shoots potatoes at 60 pounds per square inch. Can you imagine if I was deranged?
Dwight Schrute: I overslept. Damn rooster didn't crow.
Dwight Schrute: You couldn't handle my undivided attention.
Dwight Schrute: I am faster than 80% of all snakes
Dwight Schrute: Would I ever leave this company? Look, I'm all about loyalty. In fact, I feel like part of what I'm being paid for here is my loyalty. But if there were somewhere else that valued loyalty more highly… I'm going wherever they value loyalty the most.
Dwight Schrute: I am fast. To give you a reference point I am somewhere between a snake and a mongoose… And a panther.
Dwight Schrute: I have been the best salesperson in dunder mifflin for the last 10 years.
Dwight Schrute: I signed up for Second Life about a year ago. Back then, my life was so great that I literally wanted a second one. Absolutely everything was the same…except I could fly.
Dwight Schrute: As a farmer I know that when an animal is sick sometimes the right thing to do is put it out of its misery. With the electricity we are using to keep Meredith alive, we could power a small fan for two days. You tell me what's unethical.
Dwight Schrute: Last week I gave a fire safety talk. [clears throat] And nobody paid any attention. It's my own fault for using PowerPoint. PowerPoint is boring. People learn in a lot of different ways, but experience is the best teacher. [lights a cigarette] Today, smoking is gonna save lives. [throws cigarette into garbage can filled with paper and lighter fluid]

Jim Halpert: [Jim sits at his desk, dressed like Dwight]  Question, what kind of bear is best?
Dwight Schrute: That's a ridiculous question.
Jim Halpert: False. Black bear.
Dwight Schrute: Well, that's debatable. There are basically two schools of thought.
Jim Halpert: Fact, bears eat beets. Bears, beets, "Battlestar Galactica."
Dwight Schrute: Bears do not... What is going on? What are you doing?
Jim Halpert: [in confessional]  Last week, I was in a drugstore, and I saw these glasses. Four dollars. And it only cost me $7 to recreate the rest of the ensemble, and that is a grand total of $11.
Dwight Schrute: [Back at their desks]  You know what? Imitation is the most sincere form of flattery. So I thank you.
[Jim takes a bobblehead doll out of his suitcase and sets it on his desk] 
Dwight Schrute: Identity theft is not a joke, Jim! Millions of families suffer every year!
Jim Halpert: [imitating Dwight]  Michael!
Dwight Schrute: Oh, that's funny. Michael!

[Dwight comes in dressed as Jim as revenge] 
Dwight Schrute: Pam.
[drums on her desk] 
Pam Beesly: [amused]  Hey, Dwight. You look really nice today.
Dwight Schrute: [scoffs]  I look like an idiot!
[goes over to his desk] 
Dwight Schrute: He, Karen.
[flattens his hair to make it more like Jim's] 
Karen Filippelli: Hey, Dwight. Looking sharp.
Dwight Schrute: Yeah, that's 'cause I'm your boyfriend, Jim Halpert.
[Karen smiles] 
Dwight Schrute: Hey, Karen. Wanna get together later and have sexual intercourse 'cause you're my girlfriend?
Jim Halpert: [looks at Karen]  Do you?
Karen Filippelli: No. I'm good. Thanks.
Jim Halpert: Okay.
[Dwight imitates Jim's expressions; Jim is impressed] 
Jim Halpert: Look at that.
Dwight Schrute: I'm Jim Halpert.
Jim Halpert: Spot on.
Dwight Schrute: [makes some more faces and mumbles]  A little comment.

Dwight Schrute: Jim, tell him where he can stick his grapes!
Jim: In the fridge!
Dwight Schrute: No, Jim. The butt. In his butt.

Dwight Schrute: What is your name, sir?
Jim: My name is Billy Buttlicker.
Dwight Schrute: Really? That's your real name?

Jim: Dwight tried to kiss me. And I didn't tell anyone because I'm not really sure how I feel about it.
Dwight Schrute: That is not true. Redact it. Redact it!
Jim: Well I'm not actually making a formal complaint. I just really think we should talk about it.
Dwight Schrute: Michael!

Dwight Schrute: Well then. Do you have any special needs or dietary restrictions?
Jim: Yes. We will be requiring a bedtime story.
Dwight Schrute: No.
Jim: Not even Harry Potter?
Dwight Schrute: How dare you bring Harry into this!

Jim: How do you feel after that incident?
Dwight Schrute: Every day, for eight years, I have brought pepper spray into this office, to protect myself and my fellow employees. And every day, for eight years, people have laughed at me. Well, who's laughing now?

Dwight Schrute: Disconnect that right now. Give me your earpiece.
Jim: I can't do that. Unsanitary.
Dwight Schrute: Just give it to me!

Dwight Schrute: I'm going to be your new boss. It's my greatest dream come true. Welcome to Hotel Hell. Check-in time is now, checkout time is never.
Jim: Can I change rooms?
Dwight Schrute: Sorry, we're all booked up. Hell convention in town. We'll have to talk to the manager.
Jim: You're not the manager? Even in your own fantasy?
Dwight Schrute: I'm the Director! But my day-to-day operations are left to the manager!

Andy: 

Jim: you're fired
Dwight Schrute: you don't have the authority to do that Jim
Jim: yes I do, I'm co-manager
Dwight Schrute: Michael!

Jim: Michael!
Dwight Schrute: Michael!

Michael Scott: The watermark, it's a one-time thing.
Barbara Allen: I don't care! It was disgusting. Cartoon characters having sex?
Dwight Schrute: May I point out that the sex appeared to be consensual? Both animals were smiling.
Michael Scott: Okay.
Dwight Schrute: I grew up on a farm. I have seen animals having sex in every position imaginable. Goat on chicken. Chicken on goat. Couple of chickens doing a goat. Couple of pigs watching. Whoever drew this got it exactly right.

Jim: {jim_line}
Dwight Schrute:"""

@st.cache() # caching just so it's cheaper
def get_response(jim_line):
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=dwight_and_jim_prompt(jim_line),
        temperature=0.9,
    )
    return response

response = get_response(jim_line)
st.text(response.choices[0].text.split('\n')[0])

with st.expander("Not sure what to say to Dwight?"):
    st.markdown(""" 
Try some of these:
```
1. What is your name?
2. Where do you work?
3. What is the best bear?
4. Michael!
5. you're fired
6. beets are the worst vegetable
```
    """)
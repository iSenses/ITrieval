import streamlit as st
from streamlit_chat import message
from streamlit_calendar import calendar
from streamlit.components.v1 import html

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    st.session_state.generated.append("The messages from Bot\nWith new line")

def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]

audio_path = "https://docs.google.com/uc?export=open&id=16QSvoLWNxeqco_Wb2JvzaReSAw5ow6Cl"
img_path = "https://www.groundzeroweb.com/wp-content/uploads/2017/05/Funny-Cat-Memes-11.jpg"
video_embed = '''
<iframe width="400" height="215" src="https://www.bilibili.com/video/BV19E4m1X79q" title="Bilibili video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>
'''

markdown = """
### HTML in markdown is ~quite~ **unsafe**
<blockquote>
  However, if you are in a trusted environment (you trust the markdown). You can use allow_html props to enable support for html.
</blockquote>

* Lists
* [ ] todo
* [x] done

Math:

Lift($L$) can be determined by Lift Coefficient ($C_L$) like the following
equation.

$$
L = \\frac{1}{2} \\rho v^2 S C_L
$$

~~~py
import streamlit as st

st.write("Python code block")
~~~

~~~js
console.log("Here is some JavaScript code")
~~~

"""

table_markdown = '''
A Table:

| Feature     | Support              |
| ----------: | :------------------- |
| CommonMark  | 100%                 |
| GFM         | 100% w/ `remark-gfm` |
'''

st.session_state.setdefault(
    'past', 
    ['plan text with line break',
     'play the song "Dancing Vegetables"', 
     'show me image of cat', 
     'and video of it',
     'show me some markdown sample',
     'table in markdown']
)
st.session_state.setdefault(
    'generated', 
    [{'type': 'normal', 'data': 'Line 1 \n Line 2 \n Line 3'},
     {'type': 'normal', 'data': f'<audio controls src="{audio_path}"></audio>'}, 
     {'type': 'normal', 'data': f'<img width="100%" height="200" src="{img_path}"/>'}, 
     {'type': 'normal', 'data': f'{video_embed}'},
     {'type': 'normal', 'data': f'{markdown}'},
     {'type': 'table', 'data': f'{table_markdown}'}]
)

st.title("ITrieval 个人生活小助手")

cal1, chat_placeholder = st.columns([2, 3])

with chat_placeholder.container():    
    for i in range(len(st.session_state['generated'])):                
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        message(
            st.session_state['generated'][i]['data'], 
            key=f"{i}", 
            allow_html=True,
            is_table=True if st.session_state['generated'][i]['type']=='table' else False
        )
    
    st.button("Clear message", on_click=on_btn_click)

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")




mode = "daygrid"
events = [
    {
        "title": "Event 1",
        "color": "#FF6C6C",
        "start": "2024-07-03",
        "end": "2024-07-05",
        "resourceId": "a",
    },
    {
        "title": "Event 2",
        "color": "#FFBD45",
        "start": "2024-07-01",
        "end": "2024-07-10",
        "resourceId": "b",
    },
    {
        "title": "Event 3",
        "color": "#FF4B4B",
        "start": "2024-07-20",
        "end": "2024-07-20",
        "resourceId": "c",
    },
    {
        "title": "Event 4",
        "color": "#FF6C6C",
        "start": "2024-07-23",
        "end": "2024-07-25",
        "resourceId": "d",
    },
    {
        "title": "Event 5",
        "color": "#FFBD45",
        "start": "2024-07-29",
        "end": "2024-07-30",
        "resourceId": "e",
    },
    {
        "title": "Event 6",
        "color": "#FF4B4B",
        "start": "2024-07-28",
        "end": "2024-07-20",
        "resourceId": "f",
    },
    {
        "title": "Event 7",
        "color": "#FF4B4B",
        "start": "2024-07-01T08:30:00",
        "end": "2024-07-01T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 8",
        "color": "#3D9DF3",
        "start": "2024-07-01T07:30:00",
        "end": "2024-07-01T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 9",
        "color": "#3DD56D",
        "start": "2024-07-02T10:40:00",
        "end": "2024-07-02T12:30:00",
        "resourceId": "c",
    },
    {
        "title": "Event 10",
        "color": "#FF4B4B",
        "start": "2024-07-15T08:30:00",
        "end": "2024-07-15T10:30:00",
        "resourceId": "d",
    },
    {
        "title": "Event 11",
        "color": "#3DD56D",
        "start": "2024-07-15T07:30:00",
        "end": "2024-07-15T10:30:00",
        "resourceId": "e",
    },
    {
        "title": "Event 12",
        "color": "#3D9DF3",
        "start": "2024-07-21T10:40:00",
        "end": "2024-07-21T12:30:00",
        "resourceId": "f",
    },
    {
        "title": "Event 13",
        "color": "#FF4B4B",
        "start": "2024-07-17T08:30:00",
        "end": "2024-07-17T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 14",
        "color": "#3D9DF3",
        "start": "2024-07-17T09:30:00",
        "end": "2024-07-17T11:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 15",
        "color": "#3DD56D",
        "start": "2024-07-17T10:30:00",
        "end": "2024-07-17T12:30:00",
        "resourceId": "c",
    },
    {
        "title": "Event 16",
        "color": "#FF6C6C",
        "start": "2024-07-17T13:30:00",
        "end": "2024-07-17T14:30:00",
        "resourceId": "d",
    },
    {
        "title": "Event 17",
        "color": "#FFBD45",
        "start": "2024-07-17T15:30:00",
        "end": "2024-07-17T16:30:00",
        "resourceId": "e",
    },
]
calendar_resources = [
    {"id": "a", "building": "Building A", "title": "Room A"},
    {"id": "b", "building": "Building A", "title": "Room B"},
    {"id": "c", "building": "Building B", "title": "Room C"},
    {"id": "d", "building": "Building B", "title": "Room D"},
    {"id": "e", "building": "Building C", "title": "Room E"},
    {"id": "f", "building": "Building C", "title": "Room F"},
]

calendar_options = {
    "editable": "true",
    "navLinks": "true",
    "resources": calendar_resources,
    "selectable": "true",
    "headerToolbar": {
    "left": "today prev,next",
    "center": "title",
    "right": "dayGridDay,dayGridWeek,dayGridMonth",
    },
    "initialDate": "2024-07-01",
    "initialView": "dayGridMonth",
}


with cal1:
    st.subheader("日历")
    state = calendar(
    events=st.session_state.get("events", events),
    options=calendar_options,
    custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
    """,
    key=mode,
    )

    if state.get("eventsSet") is not None:
        st.session_state["events"] = state["eventsSet"]

    st.write(state)

import streamlit as st
import random as rd

def main_page():
    st.sidebar.title('main')
    st.title('3반 Diary Day (이종서)')
    
    st.markdown('- ## 구성\n'
                '   - #### 휴일\n'
                '      - 10.1(토) ~ 10.3.(월)\n'
                '   - #### 평일\n'
                '      - 교육 일상\n'
                '   - #### 마지막\n'
                '      - 여러분께 드리고픈 말\n'
                '      - 다음 발표자 선정\n')         
    st.image('diary1.jpg')

def page2():
    st.sidebar.title('휴일')
    st.title('휴일')
    st.markdown('\n'*10)
    st.image('study.jpg', width = 700)
    tab1, tab2, tab3 = st.tabs(['10.1.(토)','10.2.(일)','10.3.(월)'])
    with tab1:
        st.markdown('## 10.1(토)')
        st.markdown('#### 아침')
        st.image('헬스장3.jpg', width = 500)
        
        for i in range(8):
            st.markdown('\n')
    
        st.markdown('#### 점심')
        st.image('1001투썸.jpg', caption = 'with 연빈이형, 주영이형, 소수현님',width = 500)

        for i in range(8):
            st.markdown('\n')
            
        st.markdown('#### 저녁')
        col1, col2 = st.columns(2)
        with col1:
            st.image('1001투썸2.jpg') # 까페 공부
        with col2:
            st.image('아스날.jpg',caption = 'with 친구')

    with tab2:
        st.markdown('## 10.2.(일)')
        st.markdown('#### 아침')
        col1, col2 = st.columns(2)
        st.image('헬스장2.jpg', width = 500)
        
        for i in range(8):
            st.markdown('\n')  
            
        st.markdown('#### 점심')
        st.image('1002할리스.jpg', caption = 'with 연빈이형, 희찬이형',width = 500)

        for i in range(8):
            st.markdown('\n') 
            
        st.markdown('#### 저녁')
        col1, col2 = st.columns(2)
        with col1:
            st.image('ADP스터디.jpg') # 자격증 공부
        with col2:
            st.image('맨더비.jpg')        

    with tab3:
        st.markdown('## 10.3.(월)')
        st.markdown('#### 아침')
        col1, col2 = st.columns(2)
        with col1:
            st.image('극장판.jpg') # 
        with col2:
            st.image('짱구.jpg')
        
        for i in range(8):
            st.markdown('\n') 
            
        st.markdown('#### 점심')
        st.image('1003투썸.jpg', caption = 'with 연빈이형')

        for i in range(8):
            st.markdown('\n') 
            
        st.markdown('#### 저녁')
        col1, col2 = st.columns(2)
        with col1:
            st.image('국밥.png') # 
        with col2:
            st.image('마지막수업.jpg')        
            
def page3():
    st.sidebar.title('평일')
    st.title('평일')
    st.image('aivle.png', width = 700)
    st.markdown('\n'*10)
    st.markdown('#### 아침')
    st.image('apple.jpg', caption = '아침') # 아침 식사

    st.markdown('\n'*10)
    
    st.markdown('#### 점심')
    tab1, tab2, tab3 = st.tabs(['유형1', '유형2', '유형3'])
    with tab1:
        st.image('헬스장.jpg', width = 500) # 헬스장
    with tab2:
        st.image('산책.jpg', width = 500) # 산책
    with tab3:
        st.image('마이크.jpg', width = 500) # 노래
        
    st.markdown('\n'*10)
    
    st.markdown('#### 저녁')
    tab5, tab6 = st.tabs(['유형1', '유형2'])
    with tab5:
        st.image('호수공원.jpg', width = 500) # 호수공원
        st.image('헬스장.jpg', width = 500) # 헬스장    
    with tab6:
        st.image('클라이밍.jpg', width = 500) # 클라이밍장
        st.video('클라이밍.mp4') # 클라이밍 영상
        
def page4():
    st.sidebar.title('마지막')
    st.title('마지막')
    
    st.markdown('\n'*10)

    st.video('https://youtube.com/watch?v=WcTV_lZZPqI&feature=share&si=EMSIkaIECMiOmarE6JChQQ')
    st.markdown('\n'*10000)

    if st.button('다음 발표자는?'):
        dx3 = ['김동하','김지수','김지원','김효진','박상렬','박성연','소수현',
               '손준이','신하경','이건이','이서영','이수진','이휘재','정윤영',
               '정재나','조미예','채주영','최예찬','한재원','한주엽','황인혁','황희찬']
        a = rd.sample(dx3,1)
        st.write(str(a))
        st.image('me.gif', width = 500)

    else:
        st.write('😜'*10)
    
page_names_to_func = {'main': main_page, '휴일': page2, '평일': page3, '마지막':page4}

selected_page = st.sidebar.selectbox('page list', page_names_to_func.keys())

page_names_to_func[selected_page]()

# col1, col2, col3 = st.columns(3)
# col1.st.image()




import streamlit as st
from csv import writer
# import pyautogui
import pandas as pd
import time
import random 

# st.beta_set_page_config(page_title="secretBakra2.0",layout="wide",page_icon="🐐")
st.set_page_config(page_title="secretBakra2.0",layout="wide",page_icon="🐐")

st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">secretBakra2.0</p>', unsafe_allow_html=True)

seed = None
# seed = (3, (2971193355, 787108760, 483988240, 3315241961, 1035326907, 2415999978, 246810088, 3845308646, 1492190037, 16699422, 4122559059, 3499934418, 3505108334, 2429808449, 545580028, 274184133, 1362461002, 586852094, 50489316, 11467215, 2432506299, 1720025617, 4231396444, 2573711168, 3173503582, 3588413971, 2463191216, 348255388, 1467268703, 830615179, 3216664616, 1735753091, 2141905599, 3941158202, 975068238, 1071457505, 2679475753, 2526213822, 2776181133, 804459431, 2631496903, 1477663572, 427043629, 3868808067, 2751276044, 2394865557, 3959785235, 1416558185, 1178473533, 2348932217, 1417537217, 2793592720, 2156541813, 954771023, 2098208481, 2824290446, 2019598056, 2377477478, 332643457, 3383416407, 487775509, 2009341819, 3758346112, 473425034, 2872332041, 338792485, 3454056082, 1779134424, 2294919075, 2336424108, 1888834128, 2790549144, 1244267175, 891814361, 1067609708, 1630394865, 4289294377, 838723038, 764317158, 2758088778, 2831804020, 83130141, 937012798, 4028998363, 1882283750, 1837229105, 3596451795, 2861210133, 3734524446, 1276550166, 978542791, 2022201808, 2590401084, 1380935666, 1401981110, 217422312, 1624060279, 1857899842, 397782607, 295685729, 1854352710, 133181476, 2678440919, 1715160039, 3690020961, 366240119, 3991388417, 2314628424, 3085560933, 3983531384, 3088995503, 599574243, 1493256848, 2113883260, 719207077, 587136206, 4017397262, 2725174326, 835316937, 2359862755, 2743920033, 2977541741, 1506112417, 286030274, 482726821, 1797179355, 4278548561, 2141476312, 3042575061, 3731872862, 526841840, 3589810007, 1052869729, 908837243, 2552231809, 3014766348, 3492957260, 2580728522, 835166320, 1839407381, 1998261841, 2884053246, 3399357935, 503553802, 1719936804, 432041287, 1292282983, 1655429308, 1760784551, 2561178467, 3192692137, 27967085, 1228270767, 3798133997, 2565805931, 4226986199, 729423792, 1176920368, 1354902581, 771314439, 3126836001, 4089395705, 3389823114, 2931718056, 3993580037, 689704938, 948617790, 3272931132, 3753934457, 3902948678, 1661771598, 2817594995, 50603266, 2055869796, 2946490447, 466395668, 1299868892, 1506906690, 3592022049, 2583860605, 219518924, 2888416585, 3106984965, 2475145496, 3241503564, 2574077254, 2433461383, 634573864, 268977946, 2701707296, 2174317923, 2530334978, 142330821, 3180878889, 1623431035, 3098256114, 3118371822, 1666857140, 1060835959, 1448892025, 1779199200, 726586563, 1864012175, 2434474325, 3242929676, 2953805015, 3391312193, 3631625762, 32744597, 2598595960, 2749951398, 4081356827, 2937477340, 2133139002, 1853240915, 3180822516, 932518765, 3634680517, 2644748611, 4122074797, 3237354368, 1441832789, 2402518648, 2772465450, 2525929337, 825857899, 3885396455, 2945284871, 929232963, 120025771, 3819377881, 1395146612, 2883263594, 2733110816, 2464169654, 3264128123, 1691557157, 78025092, 948608998, 2798462563, 2610029091, 765546900, 3881305009, 3343228438, 3547359219, 3162829165, 3734236419, 2046579919, 2631943536, 30030887, 843949251, 296013082, 691035772, 3251933232, 1627067719, 109797012, 1772505231, 3120949704, 1502344005, 347724318, 2093766275, 3555175099, 903752127, 370807878, 1710574171, 1603182985, 623044471, 1166291911, 3669753566, 149971818, 3290836404, 104254224, 67694178, 3719783627, 3217989191, 2951250952, 1985401342, 3974840310, 3069544763, 1213560417, 2468885264, 931298658, 623002725, 2719844180, 293304922, 3207805874, 2285811606, 2109030054, 104813529, 3924415713, 3530266917, 1756359563, 2252962668, 3142649194, 3479339773, 3831849787, 2248876195, 2404553595, 4210821937, 1676290298, 1852566551, 3086293084, 3651145520, 2685822619, 2803630512, 667097213, 21956615, 2694543915, 3843782532, 4197035030, 3848241799, 788400127, 2444229358, 3209563669, 3304240131, 2727852820, 3379779438, 501872915, 3401048571, 2987243821, 2520194319, 2366917336, 725916077, 104193819, 87812650, 2589309946, 3216734866, 2049295197, 2163189483, 4104530556, 3449573815, 2450014702, 3058323559, 3198419911, 2459174479, 74294831, 493593972, 3052915056, 1639987590, 2074070021, 1782088369, 1969921801, 3158526150, 4219163421, 2823312421, 1861440676, 776268476, 2956995798, 1636588090, 79764164, 2750575419, 1443704926, 3915762887, 593713418, 504036939, 735027886, 2944298873, 2017370183, 1109017226, 3649598882, 3765077648, 2959084729, 1272218556, 1815755054, 2356489377, 1927690816, 346143290, 4080283975, 8797289, 1537012054, 2057901753, 4090096579, 1233990645, 1843777033, 4254787824, 1511692997, 2533675063, 160630009, 3609118272, 911933364, 3476501943, 3580496038, 2848524092, 929605601, 2924378999, 2476477711, 2427152295, 3256536628, 694163999, 1387753190, 814996630, 3891697965, 2409714977, 1675911467, 1523750618, 3834880618, 258728305, 3507784719, 1055221462, 4118478862, 2417804332, 2399404451, 1564047081, 2875075175, 3578389509, 1362959081, 3200250430, 2919495265, 353185130, 2447441830, 2367893914, 1874339659, 3431935992, 4133976756, 841305533, 3102823729, 673516020, 191340286, 3370921730, 4081808876, 2408277087, 1484500764, 2646547172, 1712693871, 3194911774, 3229656749, 2765593599, 1399612293, 770572879, 1050961833, 2115235378, 1450051497, 4012329560, 3268738981, 3865878537, 1365466905, 3862436525, 2764494968, 3799059932, 1733510192, 1939799090, 1715558855, 3252198811, 1388789550, 283300257, 978828017, 3373248986, 1878223826, 104389115, 4135343531, 2654054936, 1850256730, 3706041845, 1269484030, 2649136933, 1874611334, 1478716899, 72486550, 4004753294, 3683586230, 2964974371, 3089331110, 2662612384, 1811641204, 1113496619, 857331195, 2583882423, 291762732, 3981378166, 421876177, 2362944753, 4132769387, 3192174737, 3277746908, 1801782491, 684354221, 2275637735, 169889671, 1759242208, 1507600541, 3536186842, 552721567, 3259805871, 904788783, 2125618339, 2120598476, 188951784, 90365754, 3089293496, 5170475, 4257375890, 25786929, 1639478558, 3274695820, 4086092117, 4204450915, 822135359, 1374608150, 814422361, 3744496906, 885413976, 1710454712, 2812442100, 1701253569, 4117241078, 3725988011, 1080240797, 3001242330, 1628124735, 1474133415, 2538140017, 3095508857, 1408057371, 2768467106, 3985796769, 386230217, 3697718012, 1088364012, 1796083761, 2104127320, 602477150, 1911030099, 680573518, 1699889598, 1999037088, 3137291317, 1703127523, 3227795331, 3978100704, 3060291702, 2953444969, 65737772, 2015160999, 4255500557, 119849322, 193050980, 2332031702, 1592078034, 973314786, 2450055469, 85921353, 3006507508, 3776564838, 3815095932, 3708347601, 2234660724, 3487439814, 2178496838, 470414904, 133714415, 3119825498, 1403294904, 271519399, 4107661410, 2775185141, 3026877665, 1607584322, 627745444, 3652352477, 1232670249, 3736435952, 2312497080, 960367487, 3079135873, 2031990362, 2797029126, 687974129, 2763506276, 114090634, 3953084494, 1439909418, 1864065956, 2328077249, 3464846041, 2337244954, 1409097708, 3968478997, 1926693236, 3450246089, 1385032303, 3584172369, 1219073567, 824274681, 2593458033, 618497032, 1554299014, 2938219561, 3140227062, 1772765387, 2357509052, 2086124595, 66702623, 4080463755, 2588905345, 1885200466, 3406987806, 3981234266, 4185864245, 2481556418, 116657445, 3236570918, 1263437680, 3315552320, 436697705, 4205704240, 1449683118, 1142530757, 2864335261, 3056357752, 4287750066, 3332630130, 3131607767, 3490863319, 3411780164, 561844716, 107146799, 3939729502, 1284556210, 3939321266, 2090404574, 4011790484, 2645673755, 2666728670, 3471784363, 2), None)


def create_csv():
    
    with open("database.csv",'w',encoding="utf8",newline="") as f:
        mywriter = writer(f)
        mywriter.writerow(['First Name',"Last Name","Email","Phone No.","User Name","Password"])  
    return True

def append_to_csv(FName,LName,Email,PNo,Uname,Pass):
    with open("database.csv",'a',encoding="utf8",newline="") as f:
        mywriter = writer(f)
        mywriter.writerow([FName,LName,Email,PNo,Uname,Pass])
        f.close()
    return True  

@st.cache
def shuffle(df,state = None):
    if state == None:
        state = random.getstate()
        print(state)
    else:
        random.setstate(state)
        


    allnames = df["User Name"] 
    result = dict()
    done = []
    names = [i for i in allnames if i not in done]
    for i in range(len(allnames)):
            
        if allnames[i] in names:
            names.remove(allnames[i])
        result[allnames[i]] = random.choice(names)
        done.append([allnames[i]])
            
        names = [i for i in allnames if i not in done]
       
    return result





df = pd.read_csv("database.csv")
name = shuffle(df,seed)
rad = st.sidebar.radio("Navigation",["Home","Sign In"])

if rad == "Home":
    
    st.title("Login")
    user,pw = st.columns(2)
    usernames = df["User Name"]
    usernames = usernames.to_list()
    usernames = tuple(usernames)
    username = user.selectbox("Username",usernames,index = 0)
    password = pw.text_input("Password",type="password")

    ch,bl,log = st.columns(3)
    login = log.button("Login")

    if login:
        if True:
            u_idx = usernames.index(username)
            passwrd = df.Password[u_idx]
            if passwrd == password:
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.0005)
                    progress.progress(i+1)

                st.write(f"{username} your secret Bakra is {name[username]}")   
            else:
                st.error("Invalid password")
    st.write("""---""")
    
   
        
        
        






if rad == "Sign In":
    st.title("Registration form")
    st.info("All * fields are mandatory")

    first,last = st.columns(2)
    first = first.text_input("First Name")
    last = last.text_input("Last Name")
   

    email,mob = st.columns([3,1])
    email = email.text_input("Email ID")
    mob = mob.text_input("Mob number")
   
    
    user,pw,pw2 = st.columns(3)
    user = user.text_input("Username*")
    
    pw = pw.text_input("Password*",type="password")
    pw2 = pw2.text_input("Retype your password*",type="password")
    
    
    
    ch,bl,sub = st.columns(3)
    submit = sub.button("Submit")


    if submit:
        if ((user != "") or (pw != "") or (pw2 != "")):
            if pw == pw2:
                append_to_csv(first,last,email,mob,user,pw)
                st.success("Success")
                st.write("Please redirect to the login page...")
                time.sleep(2)
#                 pyautogui.hotkey('ctrl', 'f5')
            else:
                st.error("Passwords don't match")
        else:
            st.error("Please fill all the * credentials")

    st.write("""---""")

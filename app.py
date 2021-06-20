from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import datetime

import triangle
import myCalendar
import tele_charges
import computerSale
import atm
import theATM

st.sidebar.title('Software Test')
option = st.sidebar.selectbox(
    'Choose the question you want to test.',
    ["Types of Triangles", "Perpetual Calendar", "Computer Sales", "Telecommunication Charges", "ATM"])

st.title(option)
if option == "Types of Triangles":
    st.sidebar.markdown(triangle.description)
    option2 = st.sidebar.selectbox(
        'Test samples',
        ['Description','Boundary value analysis', 'Equivalence partition method','Customized test cases']
    )
    if option2 == 'Description':
        st.header('Description')
        st.markdown(triangle.description)
        chart_data = pd.read_csv("./triangle/三角形类型.csv", encoding="utf-8")
        st.table(chart_data)

    if option2 == 'Boundary value analysis':
        st.header('边界值法')
        st.markdown(triangle.md1)
        chart_data1 = pd.read_csv("./triangle/三角形-边界值1.csv", encoding="gbk")
        st.table(chart_data1)
        st.markdown(triangle.md2)
        chart_data2 = pd.read_csv("./triangle/三角形-边界值2.csv", encoding="gbk")
        st.table(chart_data2)

    if option2 == 'Equivalence partition method':
        st.header('等价类法')
        st.markdown(triangle.md3)
        chart_data1 = pd.read_csv("./triangle/三角形-等价类.csv", encoding="gbk")
        st.table(chart_data1)
        st.markdown(triangle.md4)
        chart_data2 = pd.read_csv("./triangle/三角形-额外弱健壮.csv", encoding="gbk")
        st.table(chart_data2)
        st.markdown(triangle.md5)
        chart_data3 = pd.read_csv("./triangle/三角形-部分额外强健壮.csv", encoding="gbk")
        st.table(chart_data3)

    if option2 == 'Customized test cases':
        st.header('输入测试用例')
        option3 = st.selectbox(
            'Test case',
            ['Input via .csv file', 'Input via textfield']
        )

        if option3 == 'Input via .csv file':
            uploaded_file = st.file_uploader("", type="csv")
            if uploaded_file is not None:
                chart_data = pd.read_csv(uploaded_file)
                if st.checkbox('Show test samples'):
                    st.write(chart_data)
            if st.button("Test"):
                st.write("Test Result")
                latest_iteration = st.empty()
                bar = st.progress(0)
                n_sample = chart_data.shape[0]
                n_right, n_wrong = 0, 0
                wrong_samples = []
                right_result = [[]]
                wrong_result = [[]]
                result = []
                real_cols = ["side 1", "side 2", "side 3","Expected", "Ground truth"]
                for i in range(1, n_sample + 1):
                    test_sample = chart_data.loc[i - 1].values
                    # decide_triangle_type 是每道题的执行函数
                    do_right, real_value, test_value = triangle.is_right(test_sample, triangle.decide_triangle_type)
                    test_sample = np.array([float(x) for x in test_sample])
                    result = np.append(test_sample, test_value)
                    if do_right:
                        n_right = n_right + 1
                        right_result = np.append(right_result, result)
                    else:
                        n_wrong = n_wrong + 1
                        wrong_result = np.append(wrong_result, result)

                    latest_iteration.text(
                        f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                    bar.progress(i / n_sample)
#                print(test_result.reshape((n_sample, 5)))
#                st.write("Passed samples")
                if len(right_result)-1 != 0:
                    st.write("Passed samples")
                    right_sample = pd.DataFrame(
                        right_result.reshape((n_right, -1)),
                        columns=real_cols)
                    st.table(right_sample)
                if len(wrong_result)-1 != 0:
                    st.write("Failed samples")
                    wrong_sample = pd.DataFrame(
                        wrong_result.reshape((n_wrong, -1)),
                        columns=real_cols)
                    st.table(wrong_sample)
                if n_right == 0:
                    st.error("All tests failed.")
                else:
                    st.warning(f"{n_right} passed. {n_wrong} failed.")
                st.header("Analysis")
                labels = 'pass', 'fail'
                sizes = [n_right, n_wrong]
                plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                plt.axis('equal')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot()

        if option3 == 'Input via textfield':
            st.write(triangle.type_of_triangle)
            sample_input = st.text_input(
                'Input your own test samples. For Example: 1,2,4:0', ' ')
            real_cols = ["side 1", "side 2", "side 3", "Expected", "Ground truth"]
            real_sample_input = re.split('[,:]', sample_input)
            real_sample_input = np.array([float(x) for x in real_sample_input])
            do_right, real_value, test_value = triangle.is_right(
                real_sample_input, triangle.decide_triangle_type)

            real_sample_input = np.append(real_sample_input, float(test_value))
            print(real_sample_input)
            new_sample = pd.DataFrame(
                real_sample_input.reshape((1, -1)),
                columns=real_cols)
            st.header('Test result')
            st.table(new_sample)



#万年历
elif option == "Perpetual Calendar":
    st.sidebar.markdown(r'''Output the date and the day of the week of the next day of the given date.''')
    option2 = st.sidebar.selectbox(
        'Test samples',
        ['Boundary value analysis', 'Equivalence partition method', 'Customized test cases']
    )
    if option2 == 'Boundary value analysis':
        st.header('边界值法')
        st.markdown(myCalendar.md1)
        chart_data1 = pd.read_csv("./myCalendar/万年历-基本边界值.csv", encoding="gbk")
        st.table(chart_data1)
        st.markdown(myCalendar.md2)
        chart_data2 = pd.read_csv("./myCalendar/万年历-健壮边界值.csv", encoding="gbk")
        st.table(chart_data2)
        st.markdown(myCalendar.md3)
        chart_data3 = pd.read_csv("./myCalendar/万年历-边界值额外测试.csv", encoding="gbk")
        st.table(chart_data3)

    if option2 == 'Equivalence partition method':
        st.header('等价类法')
        st.markdown(myCalendar.md4)
        st.markdown(myCalendar.md5)
        st.markdown(myCalendar.md6)
        chart_data1 = pd.read_csv("./myCalendar/万年历-弱一般等价类.csv", encoding="gbk")
        st.table(chart_data1)
        st.markdown(myCalendar.md7)
        chart_data2 = pd.read_csv("./myCalendar/万年历-强一般等价类.csv", encoding="gbk")
        st.table(chart_data2)
        st.markdown(myCalendar.md8)
        chart_data3 = pd.read_csv("./myCalendar/万年历-额外弱健壮.csv", encoding="gbk")
        st.table(chart_data3)

    if option2 == 'Customized test cases':
        st.header('输入测试用例')
        option3 = st.selectbox(
            'Test case',
            ['Input via .csv file', 'Input via date picker']
        )

        if option3 == 'Input via .csv file':
            uploaded_file = st.file_uploader("", type="csv")
            if uploaded_file is not None:
                date_data = pd.read_csv(uploaded_file)
                if st.checkbox('Show test samples'):
                    st.write(date_data)
            if st.button("Test"):
                st.header("Test Result")
                latest_iteration = st.empty()
                bar = st.progress(0)
                n_sample = date_data.shape[0]
                n_right, n_wrong = 0, 0
                wrong_samples = []
                right_result = [[]]
                wrong_result = [[]]
                real_cols = ["Year", "Month", "Day", "next day", "Expected", "Ground truth"]
                for i in range(1, n_sample + 1):
                    year = date_data.loc[i - 1]['year']
                    month = date_data.loc[i - 1]['month']
                    day = date_data.loc[i - 1]['day']
                    expect = date_data.loc[i - 1][' which day']
                    output, next_day = myCalendar.date_calculate(year, month, day)
                    result = []
                    result = np.append(result, [year, month, day, next_day, expect, output])
                    if expect == output:
                        n_right = n_right + 1
                        right_result = np.append(right_result, result)
                    else:
                        n_wrong = n_wrong + 1
                        wrong_result = np.append(wrong_result, result)
                    latest_iteration.text(
                        f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                    bar.progress(i / n_sample)
#                print(right_result)
#                print(wrong_result)
                if len(right_result)-1 != 0:
                    st.write("Passed samples")
                    right_sample = pd.DataFrame(
                        right_result.reshape((n_right, -1)),
                        columns=real_cols)
                    st.table(right_sample)
                if len(wrong_result)-1 != 0:
                    st.write("Failed samples")
                    wrong_sample = pd.DataFrame(
                        wrong_result.reshape((n_wrong, -1)),
                        columns=real_cols)
                    st.table(wrong_sample)
                if n_right == 0:
                    st.error("All tests failed.")
                else:
                    st.warning(f"{n_right} passed. {n_wrong} failed.")

                st.header("Analysis")
                labels = 'pass', 'fail'
                sizes = [n_right, n_wrong]
                plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                plt.axis('equal')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot()

        if option3 == 'Input via date picker':
            st.header('Input date via date picker')
            date1 = st.date_input("Select any one day", datetime.date(2021, 1, 1))
            output, next_day = myCalendar.date_calculate(date1.year, date1.month, date1.day)
            result = {'the date of next day':next_day, 'the day of next day':output}
            st.header('Test result')
            st.write(result)


#电信收费系统
elif option == "Telecommunication Charges":
    st.sidebar.write("Study a telecommunications charging system that is closely related to our lives.")
    option2 = st.sidebar.selectbox(
        "Test Samples",
        ["Description", "Boundary value analysis", 'Equivalence partition method', 'Decision table method', 'Customized test cases']
    )
    charges_data = None

    if option2 == "Description":
        st.header("Problem restatement")
        st.markdown(tele_charges.description)

    elif option2 == "Boundary value analysis":
        st.header("边界值分析法")
        st.markdown(tele_charges.boundary1)
        st.table(pd.read_csv("./tele_charges/基本边界值.csv"))
        st.markdown(tele_charges.boundary2)
        st.table(pd.read_csv("./tele_charges/健壮性边界.csv"))
        charges_data = pd.read_csv("./tele_charges/电信收费问题-边界值.csv")

    elif option2 == 'Equivalence partition method':
        st.header("等价类测试法")
        st.markdown(tele_charges.equivalence1)
        st.table(pd.read_csv("./tele_charges/强一般等价类.csv"))
        st.markdown(tele_charges.equivalence2)
        st.table(pd.read_csv("./tele_charges/额外弱健壮.csv"))
        charges_data = pd.read_csv("./tele_charges/电信收费问题-等价类.csv")

    elif option2 == 'Decision table method':
        st.header("决策表测试法")
        st.markdown(tele_charges.dt1)
        charges_data = pd.read_csv("./tele_charges/电信收费问题-扩展决策表.csv")
        st.table(charges_data)

    elif option2 == 'Customized test cases':
        st.header('输入测试用例')
        option3 = st.selectbox(
            'Test case',
            ['Input via .csv file', 'Input via textfield']
        )

        if option3 == 'Input via .csv file':
            st.header('Upload the test file')
            uploaded_file = st.file_uploader("", type="csv")
            if uploaded_file is not None:
                charges_data = pd.read_csv(uploaded_file)
                if st.checkbox('Show test samples'):
                    st.write(charges_data)
            if st.button("Test"):
                st.header("Test Result")
                latest_iteration = st.empty()
                bar = st.progress(0)
                n_sample = charges_data.shape[0]
                n_right, n_wrong = 0, 0
                right_samples = []
                wrong_samples = []
                charges_cols = ["Minutes", "overdue", "discount", "Expected", "Ground truth"]
                for i in range(1, n_sample + 1):
                    minutes = charges_data.loc[i - 1]['T']
                    n_overdue = charges_data.loc[i - 1]['M']
                    discount = charges_data.loc[i - 1]['Discount']
                    expect = charges_data.loc[i - 1]['Pay']
                    output = tele_charges.calculate_comm_fee([minutes, n_overdue, discount])
                    result = [minutes, n_overdue, discount, expect, output]
                    if float(expect) - output <= 0.01 or output == -1:
                        n_right = n_right + 1
                        right_samples = np.append(right_samples, result)
                    else:
                        n_wrong = n_wrong + 1
                        wrong_samples = np.append(wrong_samples, result)
                    latest_iteration.text(
                        f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                    bar.progress(i / n_sample)
                if n_right == n_sample:
                    right_sample = pd.DataFrame(right_samples.reshape(n_right, 5), columns=charges_cols)
                    st.write("Passed samples")
                    st.table(right_sample)
                else:
                    if n_right == 0:
                        st.error("All tests failed.")
                    else:
                        st.warning(f"{n_right} passed. {n_wrong} failed.")
                        right_sample = pd.DataFrame(right_samples.reshape(n_right, 5), columns=charges_cols)
                        st.write("Passed samples")
                        st.table(right_sample)
                    wrong_sample = pd.DataFrame(wrong_samples.reshape(n_wrong, 5), columns=charges_cols)
                    st.write("Failed samples")
                    st.table(wrong_sample)
                st.header("Analysis")
                labels = 'pass', 'fail'
                sizes = [n_right, n_wrong]
                plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                plt.axis('equal')
                st.pyplot()

        if option3 == 'Input via textfield':
            st.write('输入形式为：Minutes,Overdue,Expect,discount')
            sample_input = st.text_input('Input your own test samples. For Example: 1,3,25.15,0', ' ')
            charges_cols = ["Minutes", "overdue", "Expected", "discount", "Ground truth"]
            charges_sample_input = re.split('[,:]', sample_input)
            charges_sample_input = np.array([float(x) for x in charges_sample_input])
            output = tele_charges.calculate_comm_fee(
                [charges_sample_input[0], charges_sample_input[1], charges_sample_input[3]])
            #        print(output)
            #        print(charges_sample_input)
            charges_sample_input = np.append(charges_sample_input, float(output))
            print(charges_sample_input)
            new_sample = pd.DataFrame(
                charges_sample_input.reshape((1, -1)),
                columns=charges_cols)
            st.table(new_sample)

#ATM系统
elif option == "ATM":
    option2 = st.sidebar.selectbox(
        'Test samples',
        ['Description', 'State transition testing']
    )
    if option2 == 'Description':
        st.markdown(theATM.md1)
    elif option2 == 'State transition testing':
        st.header('State transition testing')
        st.subheader("状态图")
        atm1 = Image.open("./theATM/img/ATM.png")
        st.image(atm1, "ATM 状态图", use_column_width=True)
        st.write(theATM.state_diagram)
        st.subheader("Transition Tree")
        if st.button("run"):
            st.write(theATM.tran_tree(theATM.state_diagram))
            atm2 = Image.open("./theATM/img/ATM_2.png")
            st.image(atm2, "ATM Transition Tree", use_column_width=True)
            st.subheader("状态表")
            st.markdown(theATM.md)


#电脑销售系统
elif option == "Computer Sales":
    option2 = st.sidebar.selectbox(
        'Test samples',
        ['Description', 'Boundary value analysis', 'Customized test cases']
    )
    if option2 == 'Description':
        st.header('Description')
        st.markdown(computerSale.description)

    if option2 == 'Boundary value analysis':
        st.header('边界值法')
        st.markdown(computerSale.md1)
        chart_data = pd.read_csv("./computerSale/基本边界值.csv", encoding="gbk")
        st.table(chart_data)
        st.markdown(computerSale.md2)
        chart_data1 = pd.read_csv("./computerSale/设备健壮性边界.csv", encoding="gbk")
        st.table(chart_data1)
        st.markdown(computerSale.md3)
        st.table(pd.read_csv("./computerSale/销售额基本边界值.csv"))
        st.markdown(computerSale.md4)
        commission_data = pd.read_csv("./computerSale/佣金问题-边界值.csv")

    if option2 == 'Customized test cases':
        st.header('输入测试用例')
        option3 = st.selectbox(
            'Test case',
            ['Input via .csv file', 'Input via textfield']
        )

        if option3 == 'Input via .csv file':
            uploaded_file = st.file_uploader("", type="csv")
            if uploaded_file is not None:
                chart_data = pd.read_csv(uploaded_file)
                if st.checkbox('Show test samples'):
                    st.write(chart_data)
            if st.button("Test"):
                st.header("Test Result")
                latest_iteration = st.empty()
                bar = st.progress(0)
                n_sample = chart_data.shape[0]
                n_right, n_wrong = 0, 0
                wrong_samples = []
                right_result = [[]]
                wrong_result = [[]]
                result = []
                real_cols = ["x", "y", "z", "sale", "range type", "Expected", "Output"]
                for i in range(1, n_sample + 1):
                    x = chart_data.loc[i - 1]['x']
                    y = chart_data.loc[i - 1]['y']
                    z = chart_data.loc[i - 1]['z']
                    expect = chart_data.loc[i - 1]['commission']
                    output = computerSale.calculate_computer_commission([x, y, z])
                    test_sample = chart_data.loc[i - 1].values
                    test_sample = np.array([float(x) for x in test_sample])
                    result = np.append(test_sample, output)
                    if float(expect) == output:
                        n_right = n_right + 1
                        right_result = np.append(right_result, result)
                    else:
                        n_wrong = n_wrong + 1
                        wrong_result = np.append(wrong_result, result)

                    latest_iteration.text(
                        f'Progress: {i}/{n_sample}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                    bar.progress(i / n_sample)

                if len(right_result) - 1 != 0:
                    st.subheader("Passed samples")
                    right_sample = pd.DataFrame(
                        right_result.reshape((n_right, -1)),
                        columns=real_cols)
                    st.table(right_sample)

                if len(wrong_result) - 1 != 0:
                    st.subheader("Failed samples")
                    wrong_sample = pd.DataFrame(
                        wrong_result.reshape((n_wrong, -1)),
                        columns=real_cols)
                    st.table(wrong_sample)

                st.subheader("Analysis")
                labels = 'pass', 'fail'
                sizes = [n_right, n_wrong]
                plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                plt.axis('equal')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot()

        if option3 == 'Input via textfield':
            st.markdown(computerSale.md5)
            sample_input = st.text_input(
                'Input your own test samples. For Example: 2,1,1:12.5', ' ')
            real_cols = ["x", "y", "z", "Expected", "Output"]
            if sample_input != " ":
                real_sample_input = re.split('[,:]', sample_input)
                real_sample_input = np.array([float(x) for x in real_sample_input])
                #print(real_sample_input)
                output = computerSale.calculate_computer_commission(real_sample_input)
                real_sample_input = np.append(real_sample_input, float(output))

                new_sample = pd.DataFrame(
                    real_sample_input.reshape((1, -1)),
                    columns=real_cols)
                st.table(new_sample)
                if float(output) == real_sample_input[3]:
                    st.success(f"Test passed. ")
                    st.balloons()
                else:
                    st.error(f"Test failed. ")

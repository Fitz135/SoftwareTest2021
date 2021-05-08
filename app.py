import streamlit as st
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

import triangle
import calendar


st.sidebar.title('Software Test')
option = st.sidebar.selectbox(
    'Choose the question you want to test.',
    ["Types of Triangles", "Perpetual Calendar", "Computer Sales", "Telecommunication Charges", "C/S System"])

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
                st.table(chart_data)
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
                        right_result.reshape((n_sample, -1)),
                        columns=real_cols)
                    st.table(right_sample)
                if len(wrong_result)-1 != 0:
                    st.write("Failed samples")
                    wrong_sample = pd.DataFrame(
                        wrong_result.reshape((n_sample, -1)),
                        columns=real_cols)
                    st.table(wrong_sample)
                if n_right == n_sample:
                    text = "tests" if n_sample > 1 else "test"
                else:
                    if n_right == 0:
                        st.error("All tests failed.")
                    else:
                        st.warning(f"{n_right} passed. {n_wrong} failed.")
                    for sample in wrong_samples:
                        st.error(f"Test #{sample[2]}: {sample[3]}" +
                                 f" - Output \'{sample[1]} ({triangle.type_of_triangle[sample[1]]})\'" +
                                 f" is expected to be \'{int(sample[0])} ({triangle.type_of_triangle[sample[0]]})\'")
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
            st.table(new_sample)



#万年历
elif option == "Perpetual Calendar":
    st.sidebar.markdown(r'''Output the date and the day of the week of the next day of the given date.''')
    option2 = st.sidebar.selectbox(
        'Test samples',
        ['Description', 'Boundary value analysis', 'Equivalence partition method', 'Customized test cases']
    )


#电脑销售系统
elif option == "Computer Sales":
    st.header(option)

#电信收费系统
elif option == "Telecommunication Charges":
    st.header(option)

#万年历
elif option == "C/S System":
    st.header(option)

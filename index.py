while True:
    question = input("user: ")
    if question.lower() == "who are you":
        print("I am dummy college chat bot")

    elif question.lower() == "what can you do":
        print("I can tell you about Dummy College of Engineering")

    elif question.lower() == "what is name of college":
        print("Name of college is Dummy college of Engineering")

    elif question.lower() == "What are the admission requirements for your college":
        print("The admission requirements typically include a certain GPA, standardized test scores (such as SAT or ACT),letters of recommendation, a personal statement, and possibly an interview.")

    elif question.lower() == "Can you tell me about the available engineering programs at your college?":
        print("Our college offers a variety of engineering programs including Mechanical Engineering, Electrical Engineering, Computer Science, Civil Engineering, and more. Each program provides a comprehensive curriculum designed to prepare students for careers in their respective fields.")

    elif question.lower() == "What is the student-faculty ratio at your college?":
        print("Our college maintains a low student-faculty ratio to ensure personalized attention and support for our students. On average, we strive to maintain a ratio of 15:1, allowing students to engage closely with faculty members and receive individualized guidance.")

    elif question.lower() == "Are there any research opportunities available for undergraduate students?":
        print("Yes, our college offers various research opportunities for undergraduate students to engage in hands-on research projects under the guidance of faculty mentors. These opportunities allow students to gain valuable experience and contribute to cutting-edge research in their field of interest.")

    elif question.lower() == "Can you provide information about the average salary package offered to engineering graduates during campus placements?":
        print("The average salary package offered to engineering graduates during campus placements is INR 6-8 lakhs per annum, with some students receiving offers of up to INR 15 lakhs per annum from top-tier companies.")

    elif question.lower() == "How many companies participate in campus recruitment drives at your college?":
        print("Over 100 companies participate in campus recruitment drives at our college annually, offering a wide range of job opportunities to engineering students across various domains and specializations.")

    elif question.lower() == "How many research projects are currently underway at your college?":
        print("Our college is actively involved in research across various engineering disciplines. Currently, there are over 50 research projects underway, spanning areas such as renewable energy, artificial intelligence, sustainable infrastructure, and more.")

    elif question.lower() == " Can you provide information about the faculty-to-student ratio?":
        print("Our college maintains a favorable faculty-to-student ratio of 1:15, ensuring that students receive personalized attention and guidance from experienced faculty members.")

    elif question.lower() == "What is the acceptance rate at your college?":
        print("Our college has a competitive acceptance rate of approximately 10%, reflecting the high demand for engineering education and the rigorous admission standards.")

    elif question.lower() == "What is the average class size in engineering courses at your college?":
        print("The average class size for engineering courses at our college is approximately 60 students per class, allowing for interactive learning experiences and ample opportunities for student-faculty interaction.")

    elif question.lower() == "How many patents have been filed by faculty members and students from your college in the past year?":
        print("In the past year, faculty members and students from our college have filed a total of 25 patents, showcasing our commitment to innovation and entrepreneurship in engineering education.")

    elif question.lower() == "What percentage of engineering students participate in internships or industrial training programs?":
        print("Approximately 70% of engineering students participate in internships or industrial training programs as part of their curriculum, gaining hands-on experience and industry exposure in their respective fields of study.")

    else:
        print("question not recognised..!")
        break

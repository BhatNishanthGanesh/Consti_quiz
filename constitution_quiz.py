import tkinter as tk
from tkinter import messagebox

#100 questions
questions = [
    "What is Constitution?",
    "Who was the President of the constituent assembly?",
    "What is Preamble?",
    "When did Indian Constitution adopted & ratified in our Nation?",
    "In which system Representative to the Legislature are elected?",
    "India administered as what state?",
    "Parliamentary form of Government in India is influenced by which country?",
    "What are the aims of the Constitution of India?",
    "Fundamental Rights are given by?",
    "EQUALITY of status and of opportunity; and to promote among them all FRATERNITY assuring the dignity of the individual and",
    "When “Secular & Social” words were inserted to the preamble to our constitution?",
    "Under which amendment to the constitution Secular & Social word was inserted to the Preamble to our Constitution?",
    "When do the Citizens shall have the right to assemble?",
    "Which of the following Preamble of the Indian Constitution provides to the Citizen?",
    "Which of the following Right is not provided under Indian constitution?",
    "Which of the provision cannot be taken away by Ordinary laws?",
    "Who was the prime minister when there was amendment to the Preamble to the Constitution was adopted and accordingly inserted Secular and Socialist?",
    "Which of the state removed from the state List of Indian constitution by way of 2019 amendment to the Constitution?",
    "Who appoints as per the union Govt reference, the Governors in India?",
    "During which year the Right to Education was inserted as Fundamental Rights under the Constitution?",
    "Who was the Prime Minister of India When the Right to Education was inserted as Fundamental Rights under the Constitution?",
    "When did Emergency declared by the Indian Government.?",
    "Every person who is arrested and detained in police custody when shall the Police to produce such person before the nearest magistrate?",
    "Indian Citizens enjoy the following facility?",
    "When did ‘Jana Gana Mana Adhi Nayaka’ National Anthem was adopted in our country?",
    "The ultimate source of authority in India.",
    "Who among the following administers oath of the President of India?",
    "Socialism means",
    "Who is the Chief Justice of Supreme Court?",
    "Presently how many states are there in the State list of Indian Constitution?",
    "Under the Indian Constitution subject administration is divided into?",
    "Article 19 provides how many freedoms?",
    "Which one of the following directive principles can be described as Gandhian in nature?",
    "The ministers of the union cabinet are answerable to",
    "The speaker of the Lok Sabha",
    "One of the impediments to responsibility is",
    "This does not amount misusing the truth",
    "What is intellectual property?",
    "Which of the following is not preserved as an intellectual property",
    "An expert testimony does not demand",
    "The codes of ethics can be taken as guidelines by engineers to",
    "What is the name of the IT law that Indian is having in the Indian legislature?",
    "Under which section of IT Act, stealing any digital asset or information is written a cyber crime?",
    "What type of cyber crime, its laws and punishments does section 66 of the IT Act, 2000?",
    "Download copy, extract data from an open system done fraudulently is treated as",
    "IT Act 2008 make cyber crime details more precise where it mentioned if anyone publishes sexually explicit digital content then under..............of the IT Act, 2000 such person has to pay a legitimate amount of fine.",
    "Misuse of digital signatures for fraudulent purposes comes under.............of IT Act.",
    "The head of the Authority under IT Act is called and named as?",
    "Child pornography is punishable offence under?",
    "Repeated harassment and threatening behaviour towards someone through internet or email is known as",
    "All speeches made in the House of People are addressed to",
    "Right to privacy is contained in",
    "The Council of state in India has how many elected members",
    "The Parliament of India consists of",
    "Adjournment of the House is the power of the",
    "The Directive Principles of State Policy in the Constitution of India was adopted from",
    "Which of the following is not an objective of the Directive Principles of State Policy",
    "The President of India can dissolve the House of People on the recommendation of the",
    "How many members retired in legislative council for every two years?",
    "How many members are there in Karnataka legislative Assembly?",
    "The smoothing of irregularities to make data to look extremely precise done researches called",
    "The greatest impediment to responsibility is",
    "Conflict of Interest may be",
    "Fear --------- to responsibility",
    "The patent holder does not allow other to use potential information for years",
    "Risk estimation can be done by using",
    "Tendency of shifting responsibility will logically come down if there is",
    "Unauthorized control or access over the computer system and destroying computer data and program is known as?",
    "Public Key is used to",
    "Section 79 of I T Act declares that any 3rd party information or personal data leakage in corporate firms or organization will be a punishable offence.",
    "Revealing confidential by the professional information means",
    "The tendency of interpreting situation according to their views and imposing views",
    "What is NSPE?",
    "Which of the following is not advised by NSPE code to engineers",
    "This is not dishonesty in engineering research and testing",
    "In whose name the digital signature certificate is issued called and named as?",
    "Minimalist view means",
    "If one considers engineering profession as a building, then the following is its foundation",
    "The use of intellectual property of others without their permission is known",
    "Conflict of interest exists for an engineer when he is subject to",
    "A fault tree is used",
    "Fear is .................to responsibility.",
    "Intentionally conveying false or misleading information is",
    "System of secure key pair consisting of private key for creating a digital signature and a public key to verify digital signature is known as?",
    "What do you understand by DEMAT Account. Which statement is more appropriate one?",
    "A compound measure of the probability and magnitude of adverse effect is known as",
    "What is termed as SIM in mobile connectivity?",
    "Which is not a trade secret",
    "Protecting the expression of the ideas but not the idea itself is",
    "Secure System\" means computer hardware, software, and procedure means?",
    "As applied to engineering research and testing, relating the data to drawn a non-contradictory statement, discarding the rest is called?",
    "Good work means …",
    "The ideal fuel for modern living is an example of",
    "No code will give ...................to get solutions for ethical problems",
    "Which of the following is not considered as the aim of engineering ethics",
    "Protection of the expression of ideas but not the ideas themselves is called",
    "The Professional ethics deals with .................accepted by the professional community",
    "The diagram of the possible ways in which an accident occurs is represented by",
    "Vicarious Liability means?",
    "For an ethical engineers responsibility is"
]

#options for the question
options = [
    ["A. Ordinary Law", "B. Fundamental law of the nation", "C. Basic law book", "D. All these."],
    ["A. Dr. Rajendra Prasad", "B. Dr. B.R Ambedkar", "C. M.V Kamath", "D. Jawaharlal Nehru"],
    ["A. Explanation", "B. Introduction", "C. Conclusion", "D. Forewords"],
    ["A. 15-07-1947", "B. 26-11-1949", "C. 26-12-1949", "D. 26-01-1950"],
    ["A. Monarchy", "B. Republic", "C. Communist", "D. All the above"],
    ["A. Hindu State", "B. Secular State", "C. Communist State", "D. None of these"],
    ["A. Britain", "B. America", "C. Russia", "D. China"],
    ["A. Welfare State in India", "B. Dictatorial State", "C. Strong Nation", "D. Powerful State"],
    ["A. Parliament", "B. Supreme Court", "C. Constitution", "D. High Courts"],
    ["A. Dignity of the Citizens", "B. Unity and Integrity of the nation", "C. Social Work", "D. National Service"],
    ["A. 14-02-1951", "B. 21-12-1963", "C. 03-01-1977", "D. 01-01-1985"],
    ["A. 1st Amendment", "B. 23rd Amendment", "C. 42nd Amendment", "D. 72nd Amendment"],
    ["A. Peaceable", "B. Political Public meeting", "C. Peaceable and without arms", "D. Hunger strike."],
    ["A. Social, economic and political justice", "B. Drinking water", "C. Education", "D. Employment"],
    ["A. Social justice", "B. Economic justice", "C. Cultural justice", "D. Political justice."],
    ["A. Ordinary Rights", "B. Fundamental Rights", "C. Economic Justice", "D. Political Justice"],
    ["A. Jawahar Lal Nehru", "B. Lalbahadur Shasthri", "C. Indira Gandhi", "D. Chaudary Charan Singh"],
    ["A. Sikkim", "B. Ladakh", "C. Jammu Kashmir", "D. None of the state"],
    ["A. Members of the Legislative assembly", "B. People of the state", "C. President of India", "D. Chief Minister of the state"],
    ["A. 1976", "B. 1991", "C. 2002", "D. 2011"],
    ["A. Jawahar Lal Nehru", "B. Indira Gandhi", "C. Atal Bihari Vajapeyi", "D. Narendra Damodardas Modi"],
    ["A. 1973", "B. 1975", "C. 1974", "D. 1978"],
    ["A. Within 12 hours", "B. within 24 hours", "C. Within 48 hours", "D. Before the Closing hours of the Court."],
    ["A. Double Citizenship", "B. Single Citizenship", "C. Multi Citizenship", "D. As per the wish of the Citizen"],
    ["A. 14-07-1947", "B. 26-11-1949", "C. 24-01-1950", "D. 26-01-1950"],
    ["A. People of India", "B. Supreme Court", "C. Parliament", "D. Constitution"],
    ["A. Outgoing President of India", "B. Vice President of India", "C. Chief Justice of Supreme Court", "D. Chief Election Commissioner of India"],
    ["A. Encouraging socio economic imbalances", "B. Promotion of inter cast marriages", "C. Eradication of socio economic imbalances", "D. Discourage inter cast marriages"],
    ["A. Justice D.Y Chandrachud", "B. Justice N.V. Ramana", "C. Justice U.U Lalith", "D. Justice A.M. Khanwilkar"],
    ["A. 30", "B. 28", "C. 29", "D. 27"],
    ["A. Two Lists", "B. Three Lists", "C. Four Lists", "D. Five Lists"],
    ["A. 3", "B. 5", "C. 6", "D. 11"],
    ["A. Providing equal pay for equal work for men and women", "B. Workers' participation in management", "C. Organization of village panchayats as units of self-government", "D. Separation of judiciary from the executive."],
    ["A. The Prime Minister.", "B. The Lok Sabha.", "C. The President.", "D. The Vice-President."],
    ["A. Is appointed by the President.", "B. Is elected by the members of the Parliament.", "C. Is elected by the members of the Lok Sabha.", "D. None of the above"],
    ["A. self deception ( deception means act of cheating )", "B. rampant corruption at higher level", "C. interference by politician", "D. interference by higher officers"],
    ["A. Deliberation deception ( deception means act of cheating )", "B. biased professional information", "C. Failure to seek-out in truth", "D. withholding information"],
    ["A. Personal property", "B. Educational degree", "C. Self owned new ideas copied from other research scholars thesis", "D. Self owned research outcomes and by way of active involvement of once knowledge"],
    ["A. Copy right", "B. Government regulation", "C. Patents", "D. Trade secret"],
    ["A. adequate time for thorough investigation", "B. consultancy extensively with lawyer", "C. objective and unbiased demeanour ( demeanour meaning appearance or behaviour)", "D. expert legal knowledge"],
    ["A. Formulate the problems", "B. Resolve the conflicts", "C. Shift the responsibility", "D. Overcome the work pressure"],
    ["A. India's Technology Act, 2000", "B. India's Digital Information Technology Act, 2000", "C. The Technology Act, 2000", "D. India's Information Technology Act, 2000"],
    ["A. 65", "B. 65-D", "C. 70", "D. 67"],
    ["A. Cracking or illegally hack into any system", "B. Putting antivirus into the victim", "C. Stealing hardware components", "D. Stealing data"],
    ["A. cyber warfare", "B. cyber security act", "C. cyber crime", "D. data back up"],
    ["A. Section 66", "B. Section 67-B", "C. Section 67-A", "D. Section 67-C"],
    ["A. Section 65", "B. Section 72", "C. Section 71", "D. Section 66"],
    ["A. Controller of Certifying Authority", "B. Controller General of India", "C. Central Govt.", "D. Commissioner IT"],
    ["A. Indian Penal Code 1860", "B. POCSO Act, 2012", "C. I T Act 2000", "D. All these"],
    ["A. Cyber phishing", "B. Cyber defamation", "C. Cyber spoofing", "D. Cyber stalking"],
    ["A. The Prime Minister", "B. The Speaker", "C. Minister for Parliamentary Affairs", "D. Respective Ministers"],
    ["A. Article 22", "B. Article 19", "C. Article 21", "D. Article 22"],
    ["A. 250", "B. 238", "C. 245", "D. 230"],
    ["A. President, House of the People and Council of state", "B. House of the People and Council of states", "C. Vice President, House of People and Council of states", "D. President, Vice President, House of the People and Council of States"],
    ["A. President", "B. Speaker", "C. Prime Minister", "D. Council of Ministers Indian"],
    ["A. Irish", "B. Canada", "C. Germany", "D. Australia"],
    ["A. To ensure a welfare state", "B. to ensure socio-economic justice", "C. To establish a religious state", "D. to ensure the creation of village Panchayath"],
    ["A. Vice President", "B. Chief Justice", "C. Cabinet", "D. Council of Ministers"],
    ["A. 1/4", "B. 1/3", "C. 1/5", "D. 1/6"],
    ["A. 120", "B. 220", "C. 224", "D. 235"],
    ["A. Trimming", "B. Cooking", "C. Plagiarism", "D. Forging"],
    ["A. Rampant corruption", "B. self interest", "C. Interference by politicians", "D. Interference by higher officials."],
    ["A. Actual", "B. Imaginary", "C. Potential", "D. True"],
    ["A. a way to shift", "B. an impediment", "C. conflict", "D. both a and c"],
    ["A. 10", "B. 5", "C. 18", "D. 20"],
    ["A. Riskometer", "B. Event Tree", "C. 'R'Tree", "D. Evaluator"],
    ["A. Group thinking", "B. Microscopic vision", "C. Fear", "D. Both a and b"],
    ["A. Cracking", "B. Hacking", "C. Cyber smear", "D. Piracy"],
    ["A. Digitally sign", "B. Verify the sign", "C. Make payment", "D. Verify the documents"],
    ["A. Yes", "B. No", "C. Only if it is serious in nature", "D. No offence during first time as probationary offender"],
    ["A. Violating of patent right", "B. Criminal breach of trust", "C. Misusing the truth", "D. Breach of contract"],
    ["A. Confined vision", "B. Egocentric", "C. None of these", "D. Self interest"],
    ["A. National Service of Professional Engineers", "B. National Society of Professional Engineers", "C. National Senior Professional Engineers", "D. National Society of Professional Experts"],
    ["A. to be honest", "B. not to use firms home in dishonest business", "C. to have professional obligations", "D. not to avoid deceptive acts"],
    ["A. crimping ( giving result by joining two views)", "B. forging ( manipulation)", "C. plagiarism ( copying from other's intellectual property)", "D. cooking ( replacing actual out come with data for a favourable outcome)"],
    ["A. Customer", "B. Subscriber", "C. Controller", "D. Holder"],
    ["A. ministerial view", "B. narrow thinking", "C. novel plan to minimize industrial loss", "D. concept of Responsibility"],
    ["A. Imagination", "B. Creativity", "C. Accepting", "D. Honesty"],
    ["A. Forging", "B. Cooking", "C. Plagiarism", "D. Trimming"],
    ["A. Threat", "B. Loyalties", "C. Professional impediments", "D. Professional harassment"],
    ["A. To assess the risk involved","B. To claim compensation","C. To improve safety","D. Take free consent"],
    ["A. way of shift", "B. an impediment", "C. A conflict", "D. none of these"],
    ["A. Lying", "B. Deception", "C. Falsehood", "D. Both A and B"],
    ["A. Certification", "B. Asymmetric Crypto system", "C. Digital signature", "D. Authentication"],
    ["A. Demat Account is an account that is used to hold shares and securities in electronic format.","B. The full form of Demat account is a dematerialised account.","C. The purpose of opening a Demat account is to hold shares that have been bought or dematerialised (converted from physical to electronic shares), thus making share trading easy for the users during online trading.","D. Reserve Bank provided banking code"],
    ["A. Benefit", "B. Compensation", "C. Liability", "D. Risk"],
    ["A. Subscriber identity module", "B. Smart Identify mechanism", "C. Systematic interface module", "D. Service Integral Manager"],
    ["A. Formula", "B. Generated pattern", "C. Theorems", "D. Equipment"],
    ["A. Copy right", "B. Patent", "C. Trade Mark", "D. Plagiarism"],
    ["A. reasonably secure from unauthorized access and misuse provide a reasonable level of reliability and correct operation", "B. adhere to generally accepted security procedures", "C. Maintain legal version of software in controlling malware of the system", "D. All these"],
    ["A. Cooking", "B. Skimming", "C. Scanning", "D. Trimming"],
    ["A. Work above and beyond the call of duty", "B. Responsible work", "C. Work involving high risk", "D. Superior work done with great care and skill"],
    ["A. Trade Mark", "B. Trade Secret", "C. Copy Right", "D. Patent"],
    ["A. An Algorithm", "B. Set of ideas", "C. Ethical standards", "D. Guidelines"],
    ["A. Moral imagination", "B. Identification of ethical issues", "C. Development of analytical skills", "D. All these"],
    ["A. Copy right", "B. Plagiarism", "C. Forging", "D. Patent"],
    ["A. Scientific standards", "B. Ethical standards", "C. Technical specification", "D. Personal ethics"],
    ["A. Blue Print", "B. Fault Tree", "C. Flow Chart", "D. None of these"],
    ["A. person held liable for actions committed by him", "B. person liable for actions committed by his employees or subordinates", "C. Contract violation", "D. act committed by anyone under penal laws"],
    ["A. Legal only", "B. Moral only", "C. social only", "D. Both legal and moral"]
]

#Answers for the questions
answers = ["B", "A", "B", "B", "B", "B", "A", "A", "C", "B", "C", "C", "C", "A", "C", "B", "C", "C", "C", "C", "C", "B", "B", "B", "C", "A", "C", "C", "A", "B", "B", "C", "C", "B", "C", "A", "B", "D", "B", "D","B", "D", "A", "A", "C", "C", "B", "A", "D", "D", "B", "C", "B", "A", "B", "A", "A", "D", "B", "C", "B", "B", "C", "B", "D", "C", "C", "B", "B", "A", "D", "B", "B", "D", "A", "B", "B", "D", "C", "D", "A", "B", "D", "B", "C", "D", "A", "C", "C", "D", "A", "A", "A", "D", "C", "A", "B", "B", "B", "D"]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.question_num = 0
        
        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), command=lambda i=i: self.check_answer(chr(65 + i)))
            self.option_buttons.append(button)
            button.pack(pady=5)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=20)

        self.next_button = tk.Button(root, text="Next",font=("Arial",12), command=self.next_question)
        self.next_button.pack(pady=30)

        self.show_question()

    def show_question(self):
        question_number = self.question_num + 1  # Add 1 to question_num to display question number starting from 1
        question_text = f"{question_number}. {questions[self.question_num]}"
        self.question_label.config(text=question_text)
        for i in range(4):
            self.option_buttons[i].config(text=options[self.question_num][i])

    def check_answer(self, guess):
        if guess == answers[self.question_num]:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text="Wrong! The correct answer is: " + answers[self.question_num], fg="red")
        self.next_button.config(state=tk.NORMAL)
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)

    def next_question(self):
        self.question_num += 1
        if self.question_num < len(questions):  
            self.show_question()
            self.feedback_label.config(text="")
            for button in self.option_buttons:
                button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Result", f"Your score: {self.score}/{len(questions)}")
        self.root.destroy()

# Create GUI window
root = tk.Tk()
root.title("Quiz App")

# Set initial width and height
minimum_width = 400  
root.minsize(width=minimum_width, height=0)

# Initialize the QuizApp class
app = QuizApp(root)

# Run the GUI main loop
root.mainloop()
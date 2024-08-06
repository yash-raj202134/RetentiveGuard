# RetentiveGuard

**RetentiveGuard** is an innovative machine learning model designed to accurately detect whether an essay was written by a student or generated by a Large Language Model (LLM). This project leverages advanced natural language processing (NLP) and deep learning techniques to differentiate between human-written and LLM-generated essays, ensuring the authenticity and integrity of academic submissions.

<br><br><br>
![](image.jpeg)
## Objectives
The primary goal of RetentiveGuard is to enhance academic integrity by providing educators and institutions with a tool to verify the originality of student essays. The system aims to:

- Detect Authorship: Accurately determine whether an essay was written by a student or an LLM.
- Enhance Fairness: Ensure that all students are evaluated based on their own work, promoting fairness in academic assessment.
- Support Educators: Provide teachers and professors with a reliable tool to help in the grading process and reduce instances of academic dishonesty.
## Features

- **Essay Prompt Analysis**: Detects essays written in response to specific prompts, understanding their content and context.
- **LLM vs. Human Essay Identification**: Accurately distinguishes between essays written by students and those generated by an LLM.
- **Customizable Inputs**: Accepts essays with or without source texts, reflecting the variety of real-world scenarios.
- **Training and Testing**: Utilizes essays from two prompts for training and the remaining prompts for testing.
- **High Accuracy**: Provides high precision in distinguishing between the two essay sources.

## Dataset

The project uses a unique dataset composed of essays written in response to one of seven essay prompts:

- **Training Set**: Composed mainly of student-written essays with a few generated essays.
- **Test Set**: A hidden set of essays used to evaluate model performance.

## Methodology

The project follows a structured approach to ensure accurate and reliable results:

1. **Data Acquisition**: Collect essays written by students and those generated by LLMs.
2. **Preprocessing Data**: Clean and preprocess the data to make it suitable for model training.
3. **Model Configuration**: Set up the machine learning model with appropriate parameters.
4. **Model Training**: Train the model using the prepared training set.
5. **Model Inference**: Apply the trained model to the test set to make predictions.
6. **Post Inference Processing**: Analyze the results and refine the model as necessary.
7. **Output**: Generate a final report on model performance and accuracy.

## How to Use RetentiveGuard

Follow these steps to set up and use the RetentiveGuard model:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yash-raj202134/RetentiveGuard.git
    ```

2. **Install Dependencies**:
    - Use Conda to create and activate an environment:
        ```bash
        conda create -n retentiveguard python=3.10 -y
        conda activate retentiveguard
        ```
    - Install project requirements:
        ```bash
        pip install -r requirements.txt
        ```

3. **Prepare Data**:
    - Ensure the training and test sets are available in the specified directory.
    - The directory structure and file format should follow the guidelines provided in the project documentation.

4. **Run the Model**:
    - Use the provided scripts to preprocess data, train the model, and run inference:
        ```bash
        python preprocess_data.py
        python train_model.py
        python run_inference.py
        ```

5. **Evaluate Results**:
    - Review the output and analyze the model's performance.

## Future Directions
The development of RetentiveGuard is an ongoing process, with future enhancements aimed at:

- Improving Accuracy: Continuously refining the model to improve classification accuracy and robustness.
- Expanding Dataset: Incorporating more diverse prompts and essays to enhance the model's generalization capabilities.
- User Feedback: Incorporating feedback from educators and users to improve usability and functionality.
  
## Technologies Used

- **Python**: The primary programming language for the project.
- **TensorFlow/Keras**: Used for building and training the deep learning model.
- **NLTK/Spacy**: Utilized for natural language processing tasks.
- **Pandas/Numpy**: Employed for data manipulation and analysis.
- **Scikit-learn**: Used for model evaluation and performance metrics.
- **Jupyter Notebooks**: For exploratory data analysis and experimentation.

## Contributing

We welcome contributions from the community! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch with your changes.
3. Make a pull request to the main branch.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

Feel free to reach out with any questions or feedback:

- **Author**: Yash Raj
- **Email**: yashraj3376@gmail.com
- **LinkedIn**: [Yash Raj](https://www.linkedin.com/in/yash-raj-8b924a296/)

## Acknowledgments

- Thanks to the contributors and the open-source community for their invaluable support.
- Special thanks to my mentors and peers who provided guidance and feedback throughout the project.

---

Happy Coding!


# RetentiveGuard

**RetentiveGuard** is a machine learning model that can accurately detect whether an essay was written by a student or a Large Language Model (LLM). This innovative project leverages natural language processing and deep learning techniques to differentiate between human-written and LLM-generated essays.
<br><br><br>
![](image.jpeg)
## Features

- **Essay Prompt Analysis**: Detects essays written in response to specific prompts, understanding their content and context.
- **LLM vs. Human Essay Identification**: Accurately distinguishes between essays written by students and essays generated by an LLM.
- **Customizable Inputs**: Accepts essays with or without source texts, reflecting the variety of real-world scenarios.
- **Training and Testing**: Utilizes essays from two prompts for training and the remaining prompts for testing.
- **High Accuracy**: Provides high precision in distinguishing between the two essay sources.

## Dataset

The project uses a unique dataset composed of essays written in response to one of seven essay prompts:

- **Training Set**: Composed mainly of student-written essays with a few generated essays.
- **Test Set**: A hidden set of essays used to evaluate model performance.


## Methodology:
Steps:
-**1** Data Aquisition.
-**2** Preprocessing Data.
-**3** Model Configuration.
-**4** Model Training.
-**5** Model Inference.
-**6** Post Inference Processing.
-**7** Output.

## How to Use RetentiveGuard

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

## Contributing

We welcome contributions from the community! If you would like to contribute, please follow these steps:

- Fork the repository.
- Create a new branch with your changes.
- Make a pull request to the main branch.

## License

This project is licensed under MIT license.

## Author

[Yash Raj]  
[yashraj3376@gmail.com]


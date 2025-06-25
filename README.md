# UTMA Tax Optimizer

The UTMA Tax Optimizer is a web application built with Streamlit designed to help financial advisors and individuals manage and optimize investments within UTMA/UGMA accounts, with a focus on minimizing tax liabilities.

## Features

- **Secure Authentication**: Protects access to the application.
- **Multi-step Interface**: Guides the user through entering account info, holdings, and viewing optimization results.
- **Dynamic Holdings Input**: Easily add, edit, or delete investment positions using an interactive table.
- **Example Data**: Quickly load a sample profile to demo the application's features.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- Pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/ablewealth/UTMA-Tax-Optimizer.git](https://github.com/ablewealth/UTMA-Tax-Optimizer.git)
    cd UTMA-Tax-Optimizer
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application:**
    ```sh
    streamlit run app.py
    ```
2.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).
3.  Log in using one of the example credentials (e.g., username: `johndoe`, password: `password123`).
4.  Navigate through the steps using the sidebar to input data and view results.

## Contributing

Contributions are welcome! If you would like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix (`git checkout -b feature/your-feature-name`).
3.  Make your changes and commit them with a descriptive commit message.
4.  Push your changes to your fork (`git push origin feature/your-feature-name`).
5.  Submit a pull request.

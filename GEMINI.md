# GEMINI Project Context

## Project Overview

This project is an interactive K-Means clustering application. It allows for real-time parameter adjustment and visualization of the clustering process.

The core technologies used are:
- **Python:** The main programming language.
- **scikit-learn:** For implementing the K-Means algorithm.
- **NumPy:** For numerical operations and data generation.
- **Matplotlib:** For data visualization.

The application will feature a user interface with a control panel to adjust parameters for the data generation and K-Means algorithm, and a canvas to visualize the results.

## Building and Running

### Dependencies

The project uses `uv` for package management. The required dependencies are:
- `matplotlib`
- `numpy`
- `scikit-learn`

To install the dependencies, you can use the following command:

```bash
uv pip install -r requirements.txt 
```
**Note:** Assuming a `requirements.txt` file is generated from `pyproject.toml`.

### Running the Application

To run the application, execute the main script:

```bash
python main.py
```

### Testing

```bash
# TODO: Add command to run tests
```

## Development Conventions

- The project development is guided by the detailed specifications in `REQUIREMENTS.md`.
- The codebase should be modular, with clear separation between data handling, the user interface, and the clustering algorithm.
- Adherence to PEP 8 styling guidelines is expected.
- All significant development decisions should be documented in `DECISIONS.md`.

# Requirements Specification

## Project Overview
Interactive K-Means Clustering Application with real-time parameter adjustment and visualization. Based on E11 project but with extensive UI enhancements.

## Functional Requirements

### FR1: Package Management
- **FR1.1**: Use `uv` package manager for dependency management
- **FR1.2**: Dependencies: numpy, scikit-learn, matplotlib

### FR2: Data Generation
- **FR2.1**: Generate 6000 samples total (2000 per group)
- **FR2.2**: Three groups: A, B, C with configurable parameters
- **FR2.3**: Each group has:
  - 2D mean (x, y coordinates)
  - Standard deviation (scalar applied to both dimensions)
  - Fixed color coding:
    - Group A: RED
    - Group B: GREEN
    - Group C: BLUE

### FR3: Interactive UI Window
- **FR3.1**: Main window with two panels:
  - Left panel: Visualization canvas (matplotlib)
  - Right panel: Control widgets
- **FR3.2**: Window must be responsive and update on user actions

### FR4: Sample Size Control
- **FR4.1**: Logarithmic scrollbar for percentage control (1% - 100%)
- **FR4.2**: Affects visualization only (displays selected % of points from each group)
- **FR4.3**: K-means computation always uses full dataset (6000 points)
- **FR4.4**: Sampling should be random but consistent per percentage value

### FR5: Group Parameter Controls
- **FR5.1**: Group selector (radio buttons for A, B, C)
- **FR5.2**: 4-direction arrow buttons (↑↓←→) for mean adjustment
  - Each click adjusts mean by fixed step size
  - Up/Down adjusts Y coordinate
  - Left/Right adjusts X coordinate
- **FR5.3**: Standard deviation slider for selected group
  - Range: 1 to 10
  - Continuous adjustment
- **FR5.4**: "Regenerate Data" button to apply parameter changes
  - Changes are manual (not real-time)

### FR6: K-Means Configuration
- **FR6.1**: K value slider: integer range 2-5
- **FR6.2**: "Compute K-Means" button to trigger algorithm
- **FR6.3**: Display computation time or status

### FR7: K-Means Visualization
- **FR7.1**: Fill cluster regions with light pastel colors
- **FR7.2**: Use Voronoi-style region coloring based on cluster assignments
- **FR7.3**: Overlay data points on top of regions with original group colors
- **FR7.4**: Show cluster centroids (optional enhancement)

### FR8: Documentation Requirements
- **FR8.1**: README.md with project overview, installation, usage
- **FR8.2**: REQUIREMENTS.md (this file) with detailed specifications
- **FR8.3**: DECISIONS.md with architecture decisions (categorized)
- **FR8.4**: TODO.md with checklist format for task tracking
- **FR8.5**: CHAT.md with requirements discussion and development log
- **FR8.6**: COSTS.md for token usage and cost tracking

## Non-Functional Requirements

### NFR1: Performance
- **NFR1.1**: UI must remain responsive during K-means computation
- **NFR1.2**: Visualization updates should complete within 1 second
- **NFR1.3**: Support up to 6000 points without lag

### NFR2: Usability
- **NFR2.1**: Clear labeling of all controls
- **NFR2.2**: Intuitive layout and workflow
- **NFR2.3**: Visual feedback for user actions

### NFR3: Code Quality
- **NFR3.1**: Modular architecture (separate files for data, UI, algorithm)
- **NFR3.2**: Clear code comments and docstrings
- **NFR3.3**: Follow Python best practices (PEP 8)

### NFR4: Maintainability
- **NFR4.1**: Well-documented codebase
- **NFR4.2**: Version control with git
- **NFR4.3**: Clear project structure

## Success Criteria
1. Application launches without errors
2. All controls function as specified
3. K-means visualization accurately reflects algorithm output
4. Documentation is complete and up-to-date
5. Code is clean and maintainable

## Out of Scope
- 3D visualization
- Export functionality (save images/data)
- Multiple clustering algorithms
- Real-time K-means animation
- Undo/redo functionality

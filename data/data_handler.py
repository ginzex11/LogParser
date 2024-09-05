# data/data_handler.py

import pandas as pd
import logging

class CSVHandler:
    def __init__(self, normalization_factor: int = 500):
        self.normalization_factor = normalization_factor
        self.df = pd.DataFrame()
        self.logger = logging.getLogger(__name__)
        self.logger.debug("CSVHandler initialized.")

    def load_file(self, filepath: str):
        if not filepath:
            self.logger.warning("No file path provided to load_file.")
            return pd.DataFrame()

        try:
            self.logger.debug(f"Attempting to load file: {filepath}")
            if filepath.endswith(('.csv', '.txt')):
                self.df = pd.read_csv(filepath)
            elif filepath.endswith(('.xlsx', '.xls')):
                self.df = pd.read_excel(filepath)
            else:
                self.logger.error(f"Unsupported file format: {filepath}")
                return pd.DataFrame()
            self.logger.info(f"File loaded successfully: {filepath}")
            return self.df

        except pd.errors.EmptyDataError:
            self.logger.error(f"The file is empty: {filepath}")
            return pd.DataFrame()

        except pd.errors.ParserError:
            self.logger.error(f"Failed to parse the file: {filepath}")
            return pd.DataFrame()

        except Exception as e:
            self.logger.exception(f"An unexpected error occurred while loading file: {filepath}")
            return pd.DataFrame()

    def get_dataframe(self):
        if self.df.empty:
            self.logger.warning("No data available in DataFrame.")
        else:
            self.logger.debug("DataFrame retrieved successfully.")
        return self.df

    def process_data(self):
        if self.df.empty:
            self.logger.warning("No data to process.")
            return pd.DataFrame()
        self.logger.debug("Starting data processing.")
        processed_df = self.df.copy()
        # Example processing: normalization
        numeric_cols = processed_df.select_dtypes(include='number').columns
        processed_df[numeric_cols] = processed_df[numeric_cols] / self.normalization_factor
        self.logger.info("Data processing completed.")
        return processed_df

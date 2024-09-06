from Utils.Enums import LogLevel

class Logger:
    @staticmethod
    def info(message):
        Logger._output(LogLevel.INFO, message)

    @staticmethod
    def warning(message):
        Logger._output(LogLevel.WARNING, message)

    @staticmethod
    def error(message):
        Logger._output(LogLevel.ERROR, message)

    @staticmethod
    # This method can be used to output to multiple streams simultaneously
    # Ex: File output, logging service (Graylog, Datadog, etc)
    def _output(logLevel, message):
        output_message = f"{logLevel.name}-- {message}"
        Logger._output_to_console(output_message)

    @staticmethod
    def _output_to_console(message):
        print(message)
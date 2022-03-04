import traceback
def get_error_mess_in_ex(ex: Exception) -> (str):
    """Get message error in Exception.
    Args:
      ex: An exception given by calling the function

    Returns:
      Message with in exception

    Raises:
      ConnectionError: If no available port is found.
    """
    trace = str(traceback.format_exception(type(ex),value=ex, tb=ex.__traceback__))
    retVal = f"ERROR IN: {trace}".replace("\\n", "\n")
    return retVal


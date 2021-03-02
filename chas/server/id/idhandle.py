
# The template for creating ID handlers


class IDHandle(object):

    def __init__(self, name, desc, id_num):

        self.name = name  # Name of the handler
        self.description = desc  # Description of the handler
        self.id_num = id_num  # ID number of the handler

    def handel_server(self, dev, data):
        """
        Handle method for server operations - The socket server will call this function.

        The functionality defined within should only be relevant for server operations!

        :param dev: Device instance to handle
        :type dev: Device
        :param data: Data received from the client
        :type data: dict
        """

        pass

    def handle_server(self, dev, data):
        """
        Handle method for client operations - The socket client will call this function.

        The functionlaity defined within should only be relevant for client operations!

        If not specified, then we will redirect all requests to 'handle_server()'.

        :param dev: Device to use when handling - Usually server instance
        :type dev: Server
        :param data: Data to be handled
        :type data: dict
        """

        # Redirect content to 'handle_server()'

        self.handel_server(dev, data)

    def set_chas(self, chas):

        """
        Function for setting the CHAS Masterclass
        :param chas: Instance of the CHAS Masterclass
        :return:
        """

        self.chas = chas

    def get_id(self):

        return self.id_num
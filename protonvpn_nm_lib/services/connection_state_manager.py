
import json
import os
import time

from ..constants import CONNECTION_STATE_FILEPATH, LAST_CONNECTION_METADATA
from ..enums import ConnectionMetadataEnum


class ConnectionStateManager():
    FILEPATH = CONNECTION_STATE_FILEPATH
    LAST_CONN_FILEPATH = LAST_CONNECTION_METADATA

    def save_servername(self, servername):
        """Save connected servername metadata.

        Args:
            servername (string): servername [PT#1]
        """
        metadata = {ConnectionMetadataEnum.SERVER: servername}
        self.write_to_file(metadata)

    def save_connected_time(self):
        """Save connected time metdata."""
        metadata = self.get_connection_metadata()
        metadata[ConnectionMetadataEnum.CONNECTED_TIME] = str(int(time.time()))
        self.write_to_file(metadata)

    def save_protocol(self, protocol):
        metadata = self.get_connection_metadata()
        metadata[ConnectionMetadataEnum.PROTOCOL] = protocol
        self.write_to_file(metadata)

    def save_server_ip(self, ip):
        metadata = {
            "last_connect_ip": ip
        }
        self.write_to_file(metadata, self.LAST_CONN_FILEPATH)

    def get_server_ip(self):
        return self.get_connection_metadata(self.LAST_CONN_FILEPATH)["last_connect_ip"] # noqa

    def get_connection_metadata(self, fp=None):
        """Get connection state metadata.

        Returns:
            dict
        """
        filepath = self.FILEPATH
        if fp:
            filepath = fp
        with open(filepath) as f:
            return json.load(f)

    def write_to_file(self, metadata, fp=None):
        """Save metadata to file."""
        filepath = self.FILEPATH
        if fp:
            filepath = fp
        with open(filepath, "w") as f:
            json.dump(metadata, f)

    def remove_connection_metadata(self, fp=None):
        """Remove metadata file."""
        filepath = self.FILEPATH
        if fp:
            filepath = fp
        if os.path.isfile(filepath):
            os.remove(filepath)
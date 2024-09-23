import reflex as rx

class UploadState(rx.State):
    """The app state."""

    # The images to show.
    img: list[str]
    upload_type: str

    async def handle_upload(self, files: list[rx.UploadFile],):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)


color = "rgb(107,99,246)"
import React, { useState } from "react";

const SubmitForm = () => {
  const [image, setImage] = useState(null);
  const [text, setText] = useState("");

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    setImage(file);
  };

  const handleTextChange = (e) => {
    const value = e.target.value;
    setText(value);
  };

  const handleSubmit = () => {
    const formData = new FormData();
    formData.append("image", image);
    formData.append("text", text);

    fetch("/api/submit-form", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  };

  return (
    <form className="mt-8 mb-16 mx-auto max-w-md">
      <div className="mb-4">
        <label className="block font-bold mb-2" htmlFor="image-upload">
          Upload Image
        </label>
        <input type="file" id="image-upload" onChange={handleImageUpload} />
      </div>

      <div className="mb-4">
        <label className="block font-bold mb-2" htmlFor="text-input">
          Text Input
        </label>
        <textarea
          id="text-input"
          value={text}
          onChange={handleTextChange}
          className="w-full h-40 p-2 border rounded-lg"
        ></textarea>
      </div>

      <button
        type="button"
        onClick={handleSubmit}
        className="bg-gray-900 text-white py-2 px-4 rounded-lg hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-opacity-50"
      >
        Submit
      </button>
    </form>
  );
};

export default SubmitForm;

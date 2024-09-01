import React from "react";
import "./info.css";

export default function Info(props) {
  const { className } = props;
  return (
    <div className="mt-24 ml-10">
      <div className="container mx-auto px-4 py-6">
        <h1 className="text-2xl font-bold mb-6 text-white">
          MTIET Chatbot - College Info &#128218;
        </h1>

        <div className="text-white rounded-lg shadow-md p-6">
          <h2 className="text-2xl font-bold font-bol mb-4">About MTIET &#127891;</h2>
          <p>
          Mother Theresa Institute of Engineering and Technology, a premier Engineering College, was established in the year 2010 with the objective of developing competent and responsible technocrats for the futuristic needs of India.
          </p>
          <p>
          Promoted by "Holy Cross Educational Society, Palamaner"
          </p>
        </div>

        <div className="text-white rounded-lg shadow-md p-6">
          <h2 className="text-xl font-bold mb-4">
            Chatbot Features &#128172;
          </h2>
          <ul className="list-disc list-inside">
            <li>Instant answers to basic program queries &#128161;</li>
            <li>Customizable responses tailored to MTIET'S requirements &#128187;</li>
            <li>User-friendly interface for easy interaction &#128526;</li>
            <li>Natural Language Processing for better understanding &#128161;</li>
          </ul>
        </div>

        <div className="text-white py-4 text-center mt-6">
          <p>
            &#169; {new Date().getFullYear()} Mother Theresa Institute of Engineering and Technology &#127891;
          </p>
        </div>
      </div>
    </div>
  );
}

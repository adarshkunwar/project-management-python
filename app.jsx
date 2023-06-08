import React from "react";

const app = () => {
  return (
    <div>
      <h1>Idea generator App</h1>
      <div className="flex justify-between">
        <h2>New Ideas</h2>
        <h2>Generate an idea</h2>
      </div>

      <div className="flex justify-between">
        <div>
          {/* an already existing idea that we have already used in python*/}
        </div>
        <div>
          <button
            className="w-40 h-40 bg-red-600 rounded-full"
            onClick={() => {
              generateIdea();
            }}
          ></button>
        </div>
      </div>
    </div>
  );
};

export default app;

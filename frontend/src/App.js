import { useState, useEffect } from 'react';

function App() {
  const [content, setContent] = useState([]);

  useEffect(() => {
    fetch(process.env.REACT_APP_BACKEND_URI)
       .then((res) => res.json())
       .then((data) => {
          console.log(data);
          setContent(data);
       })
       .catch((err) => {
          console.log(err.message);
       });
  }, []);

  return (
    <div className="App">
      <p>
        {content.message}
      </p>
    </div>
  );
}

export default App;

import React, {useState, useEffect} from 'react';
import ReactDOM from 'react-dom';
import LoginGithub from 'react-login-github';
import {BrowserRouter, Outlet, Navigate, Link, useNavigate} from "react-router-dom";
import Dashboard from "./Dashboard";



const Login = () => { //changed from function
    let navigate = useNavigate();

    const [state, setState] = useState({
        auth: false
      });
  

    useEffect(() => {  //is a listener
        if(state.auth){
          console.log("Navgiate to dashboard here");
        //  BrowserRouter.navigateByUrl('/dashboard' + <Dashboard />);
            // ReactDOM.render(<Dashboard />, document.getElementById('root'));
            // navigate("/dashboard");
            //<Link  to="/dashboard" element={<Dashboard />} /> //<Link to='/queries'>Go to Queries</Link>
          //  localStorage.setItem("isLoggedin", true);
          //window.location.href = "/dashboard";
          // navigate("/dashboard");
        //    const history = createBrowserHistory();
        //    history.push({
        //     pathname:"/dashboard"});
        navigate("/dashboard");
        }
    }, [state.auth]);
    // const onSuccess = response => console.log(response);
    const onSuccess = response => {
        setState({ auth: true }); //url doesn't change, 
      //  state.auth ? ReactDOM.render(<Dashboard />, document.getElementById('root')): <h1>Please login!</h1>};
    //{ReactDOM.render(<Dashboard />, document.getElementById('root'))}; 
        //need to check if the state is authenticated or not, need to set the state to authenticated at some point
        //need to figure out what to do with callback
    };
    const onFailure = response => console.error(response); 

    return (//have the div below to be able to add headers
        <><div></div> 
      
        <LoginGithub clientId="75729dd8f6e08419c896"
            onSuccess={onSuccess} //this is a callback



            // onSuccess={ReactDOM.render(<Dashboard />, document.getElementById('root'))}
            //maybe can do something like onSuccess = this.setState...
            onFailure={onFailure} />
            
            </>

        //need to set state again when user logs out -- need a logout button?
        //look at examples I sent to Isabella with sign in and sign out button and different links
        //maybe go through a tutorial to get that working
        //state.auth ? <Outlet /> : <Navigate  to= "/" />;
    );
}

export default Login;
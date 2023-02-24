import React, { useState } from "react";
import { useSelector } from "react-redux";
import { passUpdate } from "../helper/Functions";
import { useNavigate } from "react-router-dom";

const PasswordUpdate = () => {
  const { id, access } = useSelector((state) => state.user);
  const navigate = useNavigate();
  const [passData, setPassData] = useState({
    id: id,
    access: access,
    old_password: "",
    password: "",
    password2: "",
  });
  const handleChangePas = async () => {
    await passUpdate(passData);
    navigate("/");
    setPassData({
      id: id,
      access: access,
      old_password: "",
      password: "",
      password2: "",
    });
  };
  return (
    <div
      style={{ width: "100%", height: "800px" }}
      className="d-flex justify-content-center align-items-center"
    >
      <div
        className="card text-center"
        style={{ width: "300px", height: "475px" }}
      >
        <div className="card-header h5 text-white bg-primary">
          Password Change
        </div>
        <div className="card-body px-5">
          <p className="card-text py-2 text-primary">
            Please enter your old password and new password
          </p>
          <div className="form-outline">
            <input
              onChange={(e) =>
                setPassData({ ...passData, old_password: e.target.value })
              }
              type="password"
              id="typePassword"
              className="form-control my-3"
            />
            <label className="form-label" htmlFor="typePassword">
              Old Password
            </label>
          </div>
          <div className="form-outline">
            <input
              onChange={(e) =>
                setPassData({ ...passData, password: e.target.value })
              }
              type="password"
              id="typeNewPassword"
              className="form-control my-3"
            />
            <label className="form-label" htmlFor="typeNewPassword">
              New Password
            </label>
          </div>
          <div className="form-outline">
            <input
              onChange={(e) =>
                setPassData({ ...passData, password2: e.target.value })
              }
              type="password"
              id="typeNewPassword2"
              className="form-control my-3"
            />
            <label className="form-label" htmlFor="typeNewPassword2">
              New Password2
            </label>
          </div>
          <button
            onClick={() => handleChangePas()}
            className="btn btn-primary w-100"
          >
            Update password
          </button>
          <div className="d-flex justify-content-between mt-4">
            <a className="" href="#">
              Login
            </a>
            <a className="" href="#">
              Register
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PasswordUpdate;

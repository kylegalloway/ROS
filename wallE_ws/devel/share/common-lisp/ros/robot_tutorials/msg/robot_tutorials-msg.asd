
(cl:in-package :asdf)

(defsystem "robot_tutorials-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "robot" :depends-on ("_package_robot"))
    (:file "_package_robot" :depends-on ("_package"))
  ))
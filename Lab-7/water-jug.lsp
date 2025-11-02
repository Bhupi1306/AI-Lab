;;; --- Water Jug Problem using BFS in Lisp ---

(defconstant +cap4+ 4)  ; Capacity of jug A
(defconstant +cap3+ 3)  ; Capacity of jug B
(defconstant +goal+ 2)  ; Target amount

;;; --- Helper Functions ---

(defun goal-state-p (state)
  "Check if the goal (2 gallons) is reached."
  (let ((a (first state))
        (b (second state)))
    (or (= a +goal+) (= b +goal+))))

(defun next-states (state)
  "Generate all possible valid next states from the given state."
  (let ((a (first state))
        (b (second state)))
    (remove-duplicates
     (remove-if-not
      #'(lambda (s)
          (and (<= (first s) +cap4+) (<= (second s) +cap3+)
               (>= (first s) 0) (>= (second s) 0)))
      (list
       ;; Fill either jug
       (list +cap4+ b)
       (list a +cap3+)
       ;; Empty either jug
       (list 0 b)
       (list a 0)
       ;; Pour A → B
       (let* ((spaceB (- +cap3+ b))
              (pour (min a spaceB)))
         (list (- a pour) (+ b pour)))
       ;; Pour B → A
       (let* ((spaceA (- +cap4+ a))
              (pour (min b spaceA)))
         (list (+ a pour) (- b pour))))) :test #'equal)))

;;; --- BFS Search ---

(defun bfs (start)
  "Perform BFS to find path from START to goal."
  (let ((queue (list (list start))) ; queue of paths
        (visited (list start)))
    (loop while queue do
          (let* ((path (pop queue))
                 (current (car (last path))))
            (when (goal-state-p current)
              (return path))
            (dolist (next (next-states current))
              (unless (member next visited :test #'equal)
                (push next visited)
                (push (append path (list next)) queue)))))))

;;; --- Run the Solver ---

(defun solve-water-jug ()
  "Solve and display the water jug problem."
  (let ((solution (bfs '(0 0))))
    (format t "~%Solution path (A,B):~%")
    (dolist (state solution)
      (format t "~a~%" state))))

;;; Run it
(solve-water-jug)
